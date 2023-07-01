import socket
import threading
import gui_module

# Choosing Nickname
nickname = gui_module.enter_name()
if (nickname == None):
     gui_module.no_name()

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.88.175', 33333))

# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('UTF-8')
            if message == 'NICK':
                client.send(nickname.encode('UTF-8'))
            else:
                gui_module.mess(message)
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break

def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('UTF-8'))

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()