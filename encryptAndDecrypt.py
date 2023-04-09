from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def readPrivateKey(pathKey,secretKey):
    return (RSA.import_key((open(pathKey, 'r').read()),secretKey))        

def readPublic_key(pathKey):
    return (RSA.import_key((open(pathKey, 'r').read()))).publickey()

def encrypt_with_public_key(a_message, public_key):
    return (PKCS1_OAEP.new(public_key)).encrypt(a_message)
    
def decrypt_with_private_key(encoded_encrypted_msg, private_key):
    return ((PKCS1_OAEP.new(private_key)).decrypt(encoded_encrypted_msg)).decode('latin')

""" =========== Load public and private keys =========== """
secretKey = "qwerty"
my_pub_key = readPublic_key("keys/public.pem")
my_priv_key = readPrivateKey("keys/private.pem",secretKey)

""" =========== Data to encrypt and decrypt =========== """
msn_to_encrypt = "Message to encrypt"
bytes_msn = msn_to_encrypt.encode('latin')

""" =========== Encrypt using public key =========== """
encrypt_msn = encrypt_with_public_key(bytes_msn,my_pub_key)

""" =========== Dencrypt using private key =========== """
decrypt_msn = decrypt_with_private_key(encrypt_msn,my_priv_key)