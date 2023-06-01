import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

SECRET_KEY = "123456789"
SALTVALUE = "abcdefg"

def encrypt(str_to_encrypt):
    cipher = AES.new(SECRET_KEY.encode(), AES.MODE_CBC, get_random_bytes(16))
    return base64.b64encode(cipher.encrypt(str_to_encrypt.encode())).decode()

def decrypt(str_to_decrypt):
    cipher = AES.new(SECRET_KEY.encode(), AES.MODE_CBC, base64.b64decode(str_to_decrypt)[:16])
    return cipher.decrypt(base64.b64decode(str_to_decrypt)[16:]).decode().rstrip('\0')

originalval = "pvgcoe"
encryptedval = encrypt(originalval)
decryptedval = decrypt(encryptedval)

print("Original value:", originalval)
print("Encrypted value:", encryptedval)
print("Decrypted value:", decryptedval)
