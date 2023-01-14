from socket import *

if __name__ == '__main__':
    sock = socket(family=AF_INET, type=SOCK_DGRAM)

    fp = open('example.jpg', 'rb')

    while True:
        data = fp.read(4096)
        if len(data) == 0:
            break
        sock.sendto(data, ('127.0.0.1', 12345))
    
    fp.close()
    sock.sendto(b'==========', ('127.0.0.1', 12345))
