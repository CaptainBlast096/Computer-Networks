#Things to work on
    # Allow User to decide where the file will be opened from
    # Allow User to send the file to a specified folder
    # Add DELETE Command
    # Make the FTP into the UPLOAD command
    # Create a Switch statement
import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024
SENDER_FOLDER = "/home/jaleel/Python/Desktop"
def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    
    file = open("/home/jaleel/Python/Desktop/Data", "r")
    data = file.read()

    client.send("Data.txt".encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")
    print("File has been sent to server succesfully")
if __name__== "__main__":
        main()
