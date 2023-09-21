import logging
import sys
import socket

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    PORT = 1024
    if len(sys.argv) > 1:
        PORT = int(sys.argv[1])

    sock.bind(('', PORT))
    logging.info(1024)

    sock.listen(5)

    try:
        while 1:
            client, addr = sock.accept()
            data = client.recv(1024)
            logging.info(data)
            logging.info(client)
            logging.info(addr)

            client.sendall(b'Received:' + data)
            logging.info('sent, client closing..')

            client.close()
    except BaseException as e:
        logging.error(e)

    sock.close()