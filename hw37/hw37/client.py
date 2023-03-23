#!/usr/bin/python3
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST, PORT = "localhost", 9999 
sock.connect((HOST, PORT))

while True:
    data = input("Type an operation of two numbers and an operator between them: ")
    data_bytes = data.encode() # (str to bytes)
    sock.sendall(data_bytes) # Send
    data_bytes = sock.recv(1024) # Receive
    data = data_bytes.decode() # (bytes to str)
    print("Received:", data)
