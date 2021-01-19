import socket
import sys
import threading
from datetime import datetime, timedelta
import time

HOST = 'localhost'
PORT = 5000
DELAY = 3

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))

# diff thread for input if time

def handle_client(conn, addr):
    # handle cases for different messages: stop, initial, idk if anything else
    
    while True:
        clientMessage = conn.recv(1024).decode()

        time.sleep(DELAY)

        hour, minute, second = str(datetime.now()).split(":")
        temp, hour = hour.split(" ")
        print("Server connected to " + str(addr),"\nsecond: ", second, "\nminute: ", minute, "\nhour: ", hour, flush=True)

        time.sleep(DELAY)

        current_time = str(datetime.now().time())
        conn.send(current_time.encode())

def Main():
    sock.listen()
    while True:
        conn, addr = sock.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == '__main__':
    Main()