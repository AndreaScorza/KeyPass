# KeyPass

Is a free open source password manager, which helps you to manage your passwords in a secure way.

Since KeePass was not available for older mac OS, I've created a terminal alternative using python cryptography and base64 packages. The encrypted text is stored in a local .ini file.

## Prerequisites


```bash
python v3
pip install base64
pip install cryptography
pip install argparse
pip install configparser
```

## Usage

```python
# encode password / text
python3 keyPass.py encode my secret message -key my_password -title Title -description description of the message

# decode from -title
python3 keyPass.py decode -key my_password -title Title

# decode from -message
python3 keyPass.py decode -key my_password -message gAAAAABhPgSoTlKOY0VaTorau11Dxf58IPutBarH77BUIhKoNwvcfokbVL1BR1
```

## Additional info


*  The description field is optional
* The title can be one or multiple words
* The password can be up to 32 bytes long

