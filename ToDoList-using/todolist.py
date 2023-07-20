import socket
import sys
import pickle
from utis import ADDRESS, HEADERSIZE

list_items = []


def server_socket_func(address):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(address)

    server_socket.listen(5)
    print("[*] Server started listening on port 3000...")
    while True:
        with open("list_items.txt", "a") as myfile:
            client, addr = server_socket.accept()
            print(f"Got connection from {addr}")
            new_msg = True
            full_msg = ""
            try:
                while True:
                    msg = client.recv(16)
                    if new_msg:
                        msg_len = int(msg[:HEADERSIZE])
                        new_msg = False
                    full_msg += msg.decode('utf-8')
                    if len(full_msg) - HEADERSIZE == msg_len:
                        main_msg = full_msg[HEADERSIZE:]
                        if main_msg == "show_list;":
                            msg_to_client = pickle.dumps(list_items)
                            encoded_msg = f"{len(msg_to_client) :< {HEADERSIZE}}".encode('utf-8') + msg_to_client
                            client.send(encoded_msg)
                        else:
                            list_items.append(main_msg)
                        full_msg = ""
                        new_msg = True
            except:
                for item in list_items:
                    if item != "end_list_session;":
                        myfile.write(item + "\n")
                sys.exit(0)


def client_socket_func(address):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(address)

    print("Client connected to the server.")
    print("Type 'start_list_session;' to begin.")
    on_session = True

    while on_session:
        client_command = input("$ ")

        if client_command == "start_list_session;":
            list_items = []
            while True:
                list_item = input("insert list item: ")

                if list_item == "end_list_session;":
                    sized_list_item = f"{len(list_item):<{HEADERSIZE}}" + \
                        list_item
                    client_socket.send(sized_list_item.encode('utf-8'))
                    client_socket.close()
                    print("Session ended successfully!")
                    sys.exit(0)
                else:
                    sized_list_item = f"{len(list_item):<{HEADERSIZE}}" + \
                        list_item
                    client_socket.send(sized_list_item.encode('utf-8'))
                    if list_item == "show_list;":
                        received_msg = b''
                        new_msg = True

                        while True:
                            msg = client_socket.recv(16)
                            if new_msg:
                                msg_len = int(msg[:HEADERSIZE])
                                new_msg = False
                            received_msg += msg

                            if len(received_msg) - HEADERSIZE == msg_len:
                                decoded_msg = received_msg[HEADERSIZE:]
                                accepted_msg = pickle.loads(decoded_msg)
                                for item in accepted_msg:
                                    print("  * " + item)
                                new_msg = True
                                received_msg = b''
                                break
        else:
            print("Invalid command. Type 'start_list_session;' to begin.")



if len(sys.argv) < 2:
    print("Correct usage: python3 file_name server_or_client")
elif sys.argv[1] == "server":
    server_socket_func(ADDRESS)
elif sys.argv[1] == "client":
    client_socket_func(ADDRESS)
