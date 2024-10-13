import DES
message = "hello world! this is a secret message !"
for i in range(3):
    cipher_text = DES.encrypt_cbc(message)
    print("the cipher text : ",cipher_text)

