import socket
import os

IP = socket.gethostbyname(socket.gethostname())
PORT = 4450
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024
SENDER_FOLDER = "/home/jaleel/Python/Desktop"

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    user_input = input("Enter a command: ")

    if user_input == "UPLOAD":
        # Send the "UPLOAD" command to the server
        client.send("UPLOAD".encode(FORMAT))

        # Send the file name
        client.send("Data".encode(FORMAT))

        # Then, send the file data
        file = open("/home/jaleel/Python/Desktop/Data", "r")
        data = file.read()
        client.send(data.encode(FORMAT))
        
        # Indicate the end of the file
        client.send(b'UPLOAD_COMPLETE')

        msg = client.recv(SIZE).decode(FORMAT)
        print(f"[SERVER]: {msg}")
        print("File has been sent to the server successfully")

    elif user_input == "DELETE":
         filename_to_delete = "Data"
         client.send(f"DELETE@{filename_to_delete}".encode(FORMAT))

         response = client.recv(SIZE).decode(FORMAT)
         print(f"[SERVER]: {response}")

    elif user_input == "LOGOUT":
         client.send(user_input.encode(FORMAT))
if __name__== "__main__":
        main()
