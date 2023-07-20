import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 1234))

server.listen(1)

client, addr = server.accept()


def listen():
    while True:
        msg = client.recv(100).decode('utf-8')
        print("Client:>>> " + msg)
    

def send():
    while True:
        msg = input()
        client.send(msg.encode('utf-8'))


lst_thread = threading.Thread(target=listen)
send_thread = threading.Thread(target=send)

lst_thread.start()
send_thread.start()

lst_thread.join()
send_thread.join()

