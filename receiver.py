from socket import *
from datetime import datetime

BIND_ADDR = '0.0.0.0'
BIND_PORT = 12345
FILE_PREFIX = 'photo'
PACKET_SIZE = 4096

if __name__ == '__main__':
    sock = socket(family=AF_INET, type=SOCK_DGRAM)
    sock.bind((BIND_ADDR, BIND_PORT))
    fp = None

    while True:
        if fp == None:
            now = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            fp = open(f"{FILE_PREFIX}_{now}.jpg", 'wb')
        
        data = sock.recv(PACKET_SIZE)

        if data == b'==========':
            fp.close()
        else:
            fp.write(data)
