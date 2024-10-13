from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64
import os
# Predefined 64-bit key (must be 8 bytes for DES)
KEY = b'12345678'  # 64 bits (8 bytes)

def encrypt_ecb(plaintext):
    cipher = DES.new(KEY, DES.MODE_ECB)
    padded_data = pad(plaintext.encode(), DES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    return base64.b64encode(encrypted_data).decode()

def decrypt_ecb(ciphertext):
    cipher = DES.new(KEY, DES.MODE_ECB)
    decrypted_data = unpad(cipher.decrypt(base64.b64decode(ciphertext.encode())), DES.block_size)
    return decrypted_data.decode()

def encrypt_cbc(plaintext):
    iv = os.urandom(8) 
    cipher = DES.new(KEY, DES.MODE_CBC, iv)
    padded_data = pad(plaintext.encode(), DES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    return base64.b64encode(encrypted_data).decode()

def decrypt_cbc(ciphertext):
    iv = b'abcdefgh' 
    cipher = DES.new(KEY, DES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(base64.b64decode(ciphertext.encode())), DES.block_size)
    return decrypted_data.decode()

if __name__ == "__main__":
    pass


