import socket
import struct

class ESPSocket(socket.socket):
    def __init__(self, ip, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.addr = (ip, port)
        self.error = True

    def pair(self):
        try:
            self.sock.sendto(b'\x77', self.addr)
            data, client_addr = self.sock.recvfrom(1)
            print("Paired")
            if data==b'\x77' and client_addr==self.addr:
                self.error = False
        except Exception as e:
            print(e)

            self.error = True

    def setWheelSpeed(self, w0, w1, forward):
        try:
            self.sock.sendto(struct.pack('BB?', w0, w1, forward), self.addr)
        except Exception as e:
            print(str(e))
            self.error = True


