""""
Author: Jaleel Rogers
Class: CNT3004.01
Proffesor: Dr. Dina
Title: HW #3 - Server
Date: 11/10/23
"""""
import socket
import os
import threading 

IP = socket.gethostbyname(socket.gethostname())
PORT = 4450
ADDR = (IP, PORT) #ADDR is a tupple of IP & port
FORMAT = "utf-8"
SIZE = 1024
#SERVER_PATH = "Database"
SERVER_PATH = "/home/jaleel/Python/Database"

def handle_client(conn, addr):
  print(f"[NEW CONNECTION] {addr} connected.")
  conn.send("OK@Welcome to the Server.".encode(FORMAT))

  while True:
      data = conn.recv(SIZE).decode(FORMAT)
      # print(data) # Debugging - Before input is split
      data = data.split("@")
      # print(data) # Debugging - After data is split
      cmd = data[0]
      
      if cmd == "HELP": # Issues with this command
          send_data = "OK@"
          send_data += "HELP: List all of the commands."
          send_data += "LIST: List all the files from the server.\n"
          send_data += "UPLOAD <path>: Upload a file to the server.\n"
          send_data += "DELETE <file_name>: Delete a file from the server.\n"
          send_data += "LOGOUT: Disconnect from the server.\n"

          conn.send(send_data.encode(FORMAT))

      elif cmd == "LOGOUT": 
          break
      
      elif cmd == "LIST": 
          send_data = "OK@"

          if len(files) == 0:
              send_data += "The server directory is empty."

          else:
              send_data += "\n".join (f for f in files)
          conn.send(send_data.encode(FORMAT))
      
      elif cmd == "UPLOAD": 
          name, text_file = data[1], data[2] # Organizing the data sent from client
          file_path = os.path.join(SERVER_PATH, name) # Path for server's folder
          with open(file_path, "w") as f:
              f.write(text_file)

          send_data = "OK@File uploaded succesfully." 
          conn.send(send_data.encode(FORMAT))

      elif cmd == "DELETE": 
          files = os.listdir(SERVER_PATH)
          send_data = "OK@"
          file_name = data[1]

          if len(files) == 0:
              send_data += "The server directory is empty."

          else:
              if file_name in files:
                  os.system(f"rm {SERVER_PATH}/{file_name}")
                  send_data += "Files succesfully deleted."
              else:
                  send_data += "File not found."

          conn.send(send_data.encode(FORMAT))
      
  print(f"[DISCONNECTED] {addr} disconnected")
  conn.close()

def main():
    print("[START] Server is starting.")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print("[LISTENING] Server is listening.")

    while True:
          conn, addr = server.accept()
          thread = threading.Thread(target = handle_client, args=(conn, addr)) # Responsible for server to handle multiple clients
          thread.start()
          print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__== "__main__":
        main()
