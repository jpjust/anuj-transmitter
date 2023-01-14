from socket import *

if __name__ == '__main__':
    sock = socket(family=AF_INET, type=SOCK_DGRAM)
    sock.bind(('0.0.0.0', 12345))

    fp = open('received.jpg', 'wb')

    while True:
        data = sock.recv(4096)

        if data == b'==========':
            fp.close()
            exit(0)
            
        fp.write(data)
        print('> ', end='')
        print(data)
