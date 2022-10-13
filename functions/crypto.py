from Crypto.Cipher import AES
from base64 import b64encode, b64decode
from hashlib import sha256
import os

def hash(text):
    return sha256(text.encode('utf8')).hexdigest()

def gen_key(ip):
    key = ip + os.environ.get("SECRET_KEY")[len(ip):]
    return key

def encrypt(text, ip):
    try:
        aes_obj = AES.new(gen_key(ip).encode('utf-8'), AES.MODE_CFB, os.environ.get("SALT").encode('utf8'))
        hx_enc = aes_obj.encrypt(text.encode('utf8'))
        mret = b64encode(hx_enc).decode('utf8')
        return mret
    except ValueError as value_error:
        if value_error.args[0] == 'IV must be 16 bytes long':
            raise ValueError('Encryption Error: SALT must be 16 characters long')
        elif value_error.args[0] == 'AES key must be either 16, 24, or 32 bytes long':
            raise ValueError('Encryption Error: Encryption key must be either 16, 24, or 32 characters long')
        else:
            raise ValueError(value_error)

def decrypt(text, ip):
    try:
        aes_obj = AES.new(gen_key(ip).encode('utf8'), AES.MODE_CFB, os.environ.get("SALT").encode('utf8'))
        str_tmp = b64decode(text.encode('utf8'))
        str_dec = aes_obj.decrypt(str_tmp)
        mret = str_dec.decode('utf8')
        return mret
    except ValueError as value_error:
        if value_error.args[0] == 'IV must be 16 bytes long':
            raise ValueError('Decryption Error: SALT must be 16 characters long')
        elif value_error.args[0] == 'AES key must be either 16, 24, or 32 bytes long':
            raise ValueError('Decryption Error: Encryption key must be either 16, 24, or 32 characters long')
        else:
            raise ValueError(value_error)