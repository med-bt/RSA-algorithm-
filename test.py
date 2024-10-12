import rsa

r = rsa.RSA(2048)

a = r.encrytpt("hello world my name is mohamed this is a secret message ")
b = r.decrypt(a)
print(a)
print(b)
