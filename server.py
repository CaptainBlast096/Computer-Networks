#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author : Ayesha S. Dina
import os
import socket
import threading
IP = "localhost" ### gethostname()
PORT = 4450
ADDR = (IP,PORT)
SIZE = 1024
FORMAT = "utf-8"
SERVER_PATH = "server"
### to handle the clients


def handle_client (conn,addr):
    print(f"NEW CONNECTION: {addr} connected.")
    conn.send("OK@Welcome to the server".encode(FORMAT))
    while True:
        data = conn.recv(SIZE).decode(FORMAT)
        data = data.split("@")
        cmd = data[0]
        send_data = "OK@"
        if cmd == "LOGOUT":
            break

        if cmd == "NEWFOLDER":
            send_data += "Enter the folder name: "
            conn.send(send_data.encode(FORMAT))
            try:
                folder_name = conn.recv(SIZE).decode(FORMAT)
                os.mkdir(f"{SERVER_PATH}/{folder_name}")
                send_data += f"Folder {folder_name} is created successfully.\n"
                conn.send(send_data.encode(FORMAT))

            except FileExistsError: #If the file already exists
                send_data += f"Folder {folder_name} is already exists.\n"
                conn.send(send_data.encode(FORMAT))

            except FileNotFoundError: #If the file is not found
                send_data += f"Folder {folder_name} is not found.\n"
                conn.send(send_data.encode(FORMAT))

        elif cmd == "TASK":
            send_data += "LOGOUT from the server.\n"
            conn.send(send_data.encode(FORMAT))

    print(f"{addr} disconnected")
    conn.close()
def main():
    print("Starting the server")
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) ## used IPV4 and TCP connection
    server.bind(ADDR) # bind the address
    server.listen() ## start listening
    print(f"server is listening on {IP}: {PORT}")
    while True:
        conn, addr = server.accept() ### accept a connection from a client
        thread = threading.Thread(target = handle_client, args = (conn, addr)) ## assigning a thread for each client
        thread.start()

if __name__ == "__main__":
    main()