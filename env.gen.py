import sys
from Crypto.Cipher import AES
from getpass4 import getpass
from base64 import b64encode, b64decode


def get_key():
    key = getpass("Enter Passphrase: ")
    while (len(key) < 32):
        key += key
    return key[:32]


def get_salt():
    key = getpass("Enter Salt: ")
    while (len(key) < 16):
        key += key
    return key[:16]


def encrypt():
    try:
        with open('.env', 'r') as read_file:
            key = get_key()
            salt = get_salt()
            aes_obj = AES.new(key.encode('utf-8'), AES.MODE_CFB,
                              salt.encode('utf8'))
            print("[1/3] Encrypting .env file")
            with open('env.gen.data', 'w') as write_file:
                lines = read_file.readlines()
                print("[2/3] Writing to env.gen.data")
                for line in lines:
                    hx_enc = aes_obj.encrypt(line.encode('utf8'))
                    mret = b64encode(hx_enc).decode('utf8')
                    write_file.write(mret+"\n")
        print("[3/3] .env file encrypted successfully")
    except Exception as e:
        if 'No such file or directory' in str(e):
            print('ERROR! No .env file found to encrypt')


def decrypt():
    try:
        key = get_key()
        salt = get_salt()
        aes_obj = AES.new(key.encode('utf-8'), AES.MODE_CFB,
                          salt.encode('utf8'))
        print("[1/3] Decrypting env.gen.data")
        with open('env.gen.data', 'r') as read_file:
            with open('.env', 'w') as write_file:
                lines = read_file.readlines()
                for line in lines:
                    str_tmp = b64decode(line.encode('utf8'))
                    str_dec = aes_obj.decrypt(str_tmp)
                    mret = str_dec.decode('utf8')
                    write_file.write(mret)
                print("[2/3] Writing to .env")
        print("[3/3] env.gen.data decrypted successfully")
    except Exception as e:
        if 'codec can\'t decode byte' in str(e):
            print('ERROR! Invalid key or salt')
            print('Make sure you are using the same key and salt as used to encrypt the file or it may result in permanent data loss')


what = sys.argv[1]
if what == 'encrypt':
    encrypt()
elif what == 'decrypt':
    decrypt()
else:
    print('Invalid argument')
