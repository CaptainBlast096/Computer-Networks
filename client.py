#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author : Ayesha S. Dina
import os
import socket
IP = "localhost"
PORT = 4450
ADDR = (IP,PORT)
SIZE = 1024 ## byte .. buffer size
FORMAT = "utf-8"
SERVER_DATA_PATH = r"C:\Database"
def main():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(ADDR)
    while True: ### multiple communications
        data = client.recv(SIZE).decode(FORMAT)
        cmd, msg = data.split("@")
        if cmd == "OK":
            print(f"{msg}")
        elif cmd == "DISCONNECTED":
            print(f"{msg}")
            break

        data = input("> ")
        data = data.split(" ")
        cmd = data[0]

        if cmd == "TASK":
            client.send(cmd.encode(FORMAT))

        elif cmd == "UPLOAD":
           file = open (SERVER_DATA_PATH, "r")
           data = file.read()

           client.send("yt.txt".encode(FORMAT))
           msg = client.recv(SIZE).decode(FORMAT)
           print(f"[SERVER]: {msg}")
           client.send(data.encode(FORMAT))
           msg = client.recv(SIZE).decode(FORMAT)
           print(f"[SERVER]: {msg}")
           file.close()

        elif cmd == "LOGOUT":
            client.send(cmd.encode(FORMAT))
            break

    print("Disconnected from the server.")
    client.close() ## close the connection

if __name__ == "__main__":
    main()