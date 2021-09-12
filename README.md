# KeyPass

Since KeyPass was not available for older mac OS, I've created mine using python cryptography and base64 packages

Usages:

- python3 keyPass.py encode my secret message -key my_password -title Title -description description of the message
- python3 keyPass.py decode -key my_password -title Title
- python3 keyPass.py decode -key my_password -message gAAAAABhPgSoTlKOY0VaTorau11Dxf58IPutBarH77BUIhKoNwvcfokbVL1BR1jVha1EnmRcieAaZPaiUHqjJNCOsRUGhj-3kYeS3hI2fMarH96VHckGJoM=

. the description field is optional
. the title can be one or multiple words
. the password can be up to 32 bytes long
