from socket import *
from picamera import PiCamera
import time

SHOOTING_INTERVAL = 1
TMP_IMG = 'img.jpg'
PACKET_SIZE = 4096
RECEIVER_ADDR = '192.168.0.114'
RECEIVER_PORT = 12345

if __name__ == '__main__':
    camera = PiCamera()

    while True:
        try:
            sock = socket(family=AF_INET, type=SOCK_STREAM)
            sock.connect((RECEIVER_ADDR, RECEIVER_PORT))
            
            while True:
                time.sleep(SHOOTING_INTERVAL)
                camera.capture(TMP_IMG)
                fp = open(TMP_IMG, 'rb')
                
                while True:  # Transmission loop
                    data = fp.read(PACKET_SIZE)
                    
                    if len(data) == 0:
                        break

                    sock.send(data)
                
                fp.close()
                sock.send(b'--- photo delimiter ---')
                print('shoot!')
        except ConnectionRefusedError:
            print('connection refused')
            time.sleep(SHOOTING_INTERVAL)
        except BrokenPipeError:
            print('broken pipe')
            time.sleep(SHOOTING_INTERVAL)
        except OSError:
            print('os error')
            time.sleep(SHOOTING_INTERVAL)
