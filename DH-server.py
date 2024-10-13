import socket
import random
p = 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171
g = 555555555555555555
def generate_private_key():
    return random.randint(1, p - 1)

def calculate_public_key(private_key):
    return pow(g, private_key, p)

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5000))
    server_socket.listen(1)
    print("Server listening on port 5000...")
    conn, addr = server_socket.accept()
    print(f"Connected to client at {addr}")
    private_key = generate_private_key()
    public_key = calculate_public_key(private_key)
    conn.send(str(public_key).encode())
    client_public_key = int(conn.recv(1024).decode())
    shared_secret = pow(client_public_key, private_key, p)
    print("Shared Secret Key (Server):", shared_secret)
    conn.close()
    server_socket.close()
if __name__ == "__main__":
    main()
