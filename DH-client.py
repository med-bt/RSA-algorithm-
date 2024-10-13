import socket
import random
p = 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171
g = 555555555555555555 
def generate_private_key():
    return random.randint(1, p - 1)
def calculate_public_key(private_key):
    return pow(g, private_key, p)
def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5000))
    private_key = generate_private_key()
    public_key = calculate_public_key(private_key)
    server_public_key = int(client_socket.recv(1024).decode())
    client_socket.send(str(public_key).encode())
    shared_secret = pow(server_public_key, private_key, p)
    print("Shared Secret Key (Client):", shared_secret)
    client_socket.close()
if __name__ == "__main__":
    main()
