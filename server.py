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
SERVER_PATH = r"C:\Database"
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

        elif cmd == "UPLOAD":
            filename = data[1]
            try:
                print(f"[RECV] Receviing the filename: {filename}")
                conn.send("Filename recieved.".encode(FORMAT))

                file_data = conn.recv(SIZE).decode(FORMAT)
                print(f"[RECV] Receviing the file data.")

                with open(filename, "w") as file:
                    file.write(file_data)

                conn.send("File data received.".encode(FORMAT))
                print(f"[SAVE] File {filename} saved.")
            except Exception as e:
                error_message = f"File {filename} not saved. Error: {e}"
                print(error_message)
                conn.send(error_message.encode(FORMAT))
            else:
                print("Invalid UPLOAD command. Usage: UPLOAD <filename>")

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