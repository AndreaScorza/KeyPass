from copy import copy
import configparser
import os
from cryptography.fernet import Fernet
import base64
import argparse


def main():
    parser = argparse.ArgumentParser(description='Key Pass:'
    'To encrypt: write the message that will be encrypted, followed by the  -key, and a -title under which it will be saved. You can add an optional -description'
    'To decrypt: -key, -message (to decrypt) or -title (of the message to decrypt)')

    parser.add_argument('list', type=str, nargs='+')
    parser.add_argument('-key', type=str, nargs=1, required=True)
    parser.add_argument('-message', type=str, nargs=1)
    parser.add_argument('-title', type=str, nargs='+')
    parser.add_argument('-description', type=str, nargs='+')

    args = parser.parse_args()

    list = args.list
    key = args.key[0]
    message = args.message[0] if args.message else ''
    title = args.title
    description = args.description

    if list[0] not in ['encode', 'decode']:
        raise Exception('First parameter should be Encode or Decode')

    if list[0] == 'encode':
        if not title:
            raise Exception('Required Title')

        token = Fernet(get32bitKey(key)).encrypt(getTheMessage(list)).decode('utf8')
        print(token)
        saveToken(token, title, description)

    else:  # decode case
        if not message and not title:
            raise Exception('Required Message or Title')
        if message:
            print(Fernet(get32bitKey(key)).decrypt(str.encode(message)).decode('utf8'))
        else:
            config = configparser.ConfigParser()
            config.read('config.ini')
            if ' '.join(map(str, title)) not in config.sections():
                raise Exception('No token found matching with the title')
            else:
                message = config.get(' '.join(map(str, title)), 'token')
                print(Fernet(get32bitKey(key)).decrypt(str.encode(message)).decode('utf8'))



def saveToken(token, title, description):
    title = ' '.join(map(str, title))
    config = configparser.ConfigParser()
    if os.path.exists('../../config.ini'):
        config.read('config.ini')
        if title in config.sections():
            raise Exception("Title already present")
    config.add_section(title)
    config.set(title, 'token', token)
    if description:
        config.set(title, 'description', ' '.join(map(str, description)))
    config.write(open('../../config.ini', 'w'))



def get32bitKey(input):
    while len(input) < 32:
        input = input + '0'
    return base64.urlsafe_b64encode(str.encode(input))

def getTheMessage(phrase):
    output = copy(phrase)
    output.pop(0)
    return str.encode(' '.join(map(str, output)))

if __name__ == '__main__':
    main()