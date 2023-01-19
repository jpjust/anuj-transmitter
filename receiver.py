from socket import *
from datetime import datetime

BIND_ADDR = '0.0.0.0'
BIND_PORT = 12345
PHOTOS_FOLDER = 'photos'
PHOTOS_PREFIX = 'photo'
PACKET_SIZE = 4096

if __name__ == '__main__':
    sock = socket(family=AF_INET, type=SOCK_STREAM)
    sock.bind((BIND_ADDR, BIND_PORT))
    sock.listen()
    conn, addr = sock.accept()
    fp = None
    filename = ''

    while True:
        data = conn.recv(PACKET_SIZE)

        if fp == None or fp.closed:
            now = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            filename = f"{PHOTOS_FOLDER}/{PHOTOS_PREFIX}_{now}.jpg"
            fp = open(filename, 'wb')

        if data.endswith(b'--- photo delimiter ---'):
            fp.write(data.rstrip(b'--- photo delimiter ---'))
            fp.close()
            print(f'saved {filename}')
        else:
            fp.write(data)
