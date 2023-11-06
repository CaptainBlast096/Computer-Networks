import socket
import os

IP = socket.gethostbyname(socket.gethostname())
PORT = 4450
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024
DESTINATION_FOLDER = "/home/jaleel/Python/Database"

def recieve_file(conn):
      # Receive the file name from the client
    filename = conn.recv(SIZE).decode(FORMAT)

    # Inform the client that the server is ready to receive the file
    conn.send("READY".encode(FORMAT))

    # Set the file path in the destination folder
    file_path = os.path.join(DESTINATION_FOLDER, filename)

    with open(file_path, "wb") as file:
        while True:
            data = conn.recv(SIZE)
            if data == b'UPLOAD_COMPLETE':
                break
            file.write(data)

    # Inform the client that the file transfer is complete
    conn.send("File uploaded successfully".encode(FORMAT))

def delete_file(conn):
    file_delete = "Data"
    file_path = os.path.join(DESTINATION_FOLDER, file_delete)
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            response = "File deleted successfully."
        except Exception as e:
            response = f"Error deleting file: {str(e)}"
    else:
        response= "File not found."
    print(f"Sending response: {response}")
    conn.send(response.encode(FORMAT))

def main():
    print("[START] Server is starting.")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print("[LISTENING] Server is listening.")

    while True:
          conn, addr = server.accept()
          print(f"[NEW CONNECTION] {addr} connected.")
          command = conn.recv(SIZE).decode(FORMAT)

          if command == "UPLOAD":
            recieve_file(conn)

          if command == "DELETE":
            print("Will delete file from server's database")
            delete_file(conn)

          if command == "LOGOUT":
            print(f"{addr} disconnected")
            break
          conn.close
        
if __name__== "__main__":
        main()
