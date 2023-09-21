import socket
import sys

if __name__ == '__main__':
    try:
        HOST = sys.argv[1]
    except:
        HOST = '0.0.0.0'

    try:
        PORT = int(sys.argv[2])
    except:
        PORT = 1024

    # Define the server address and port
    server_address = (HOST, PORT)

    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print('connecting...')

    # Connect to the server
    sock.connect(server_address)
    print('connected')

    # Send and receive data over the SSL socket
    sock.send(b"hi server")
    response = sock.recv(1024)
    print(response)

    # Close the SSL socket
    sock.close()

