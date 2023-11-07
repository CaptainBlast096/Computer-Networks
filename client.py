""""
Author: Jaleel Rogers
Class: CNT3004.01
Proffesor: Dr. Dina
Title: HW #3 - Server
Date: 11/10/23
"""""
import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 4450
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024
SENDER_FOLDER = "/home/jaleel/Python/Desktop" # Not needed in program

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    
    while True:
        data = client.recv(SIZE).decode(FORMAT)
        cmd, msg = data.split("@")

        if cmd == "DISCONNECTED":
             print(f"[SERVER]: {msg}")
             break
        
        elif cmd == "OK":
             print(f"{msg}")

        data = input("> ") 
        data = data.split(" ") # Splitting by space
        cmd = data[0]

        if cmd == "HELP":
            client.send(cmd.encode((FORMAT)))
        
        elif cmd == "LOGOUT":
            client.send(cmd.encode(FORMAT))
            break
        
        elif cmd == "LIST": 
            client.send(cmd.encode(FORMAT))
        
        elif cmd == "UPLOAD":
            path = data[1]

            with open(f"{path}", "r") as f:
                text_file = f.read()
            
            file_name = path.split("/")[-1]
            send_data = f"{cmd}@{file_name}@{text_file}"
            client.send(send_data.encode(FORMAT))

        elif cmd == "DELETE":
            client.send(f"{cmd}@{data[1]}".encode(FORMAT))
        
    print("Disconnected from the server.")
    client.close()
        
if __name__== "__main__":
        main()
