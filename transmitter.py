from socket import *
from picamera import PiCamera
import time

SHOOTING_INTERVAL = 10
TMP_IMG = 'img.jpg'
PACKET_SIZE = 4096
RECEIVER_ADDR = '127.0.0.1'
RECEIVER_PORT = 12345

if __name__ == '__main__':
    sock = socket(family=AF_INET, type=SOCK_DGRAM)
    camera = PiCamera()

    while True:  # Camera loop
        time.sleep(SHOOTING_INTERVAL)
        camera.capture(TMP_IMG)
        fp = open(TMP_IMG, 'rb')

        while True:  # Transmission loop
            data = fp.read(PACKET_SIZE)
            
            if len(data) == 0:
                break

            sock.sendto(data, (RECEIVER_ADDR, RECEIVER_PORT))
        
        fp.close()
        sock.sendto(b'==========', (RECEIVER_ADDR, RECEIVER_PORT))
