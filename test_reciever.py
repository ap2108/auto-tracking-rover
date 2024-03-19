import struct
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("",1235))
_,c = sock.recvfrom(1)
print("Recieved pairing")
sock.sendto(b'\x77',c)
print("Sent pairing")

while True:
    data,c = sock.recvfrom(5)
    data = struct.unpack('BBBB?', data)
    print(data)

