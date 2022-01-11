import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 1234))

def listen():
    try:
        while True:
            msg = client.recv(100).decode('utf-8')
            print("Client:>>> " + msg + "\n")
    except:
        pass

def send():
    try:
        while True:
            msg = input()
            client.send(msg.encode('utf-8'))
    except:
        pass


lst_thread = threading.Thread(target=listen)
send_thread = threading.Thread(target=send)

lst_thread.start()
send_thread.start()

lst_thread.join()
send_thread.join()
