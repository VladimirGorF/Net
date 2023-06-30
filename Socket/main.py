import socket
import threading
from time import sleep

ya_sock = socket.socket()
addr = ("5.255.255.242", 443)
ya_sock.connect(addr)
data_out = b"GET / HTTP/1.1\r\nHost:ya.ru\r\n\r\n"
ya_sock.send(data_out)

data_in = b""

def recieving():
    global data_in
    while(True):
        data_in = data_in + ya_sock.recv(1024)
        print(data_in)


rec_thread = threading.Thread(target=recieving)
rec_thread.start()

sleep(4)
print(data_in)

ya_sock.close

