import os
import socket

# IP = "192.168.1.101" #"localhost"
IP = "localhost"
PORT = 4450
ADDR = (IP, PORT)
SIZE = 1024  ## byte .. buffer size
FORMAT = "utf-8"
SERVER_DATA_PATH = r"C:\Database"


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    while True:  ### multiple communications
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
            filename = data[1]
            try:
                with open(SERVER_DATA_PATH, 'r') as file:
                    file_data = file.read()
                    client.send(filename.encode(FORMAT))
                    msg = client.recv(SIZE).decode(FORMAT)
                    print(f"[SERVER]: {msg}")
                    client.send(file_data.encode(FORMAT))
                    msg = client.recv(SIZE).decode(FORMAT)
                    print(f"[SERVER]: {msg}")
            except FileNotFoundError:
                print(f"File '{filename}' not found.")

        elif cmd == "LOGOUT":
            client.send(cmd.encode(FORMAT))
            break

    print("Disconnected from the server.")
    client.close()  ## close the connection


if __name__ == "__main__":
    main()