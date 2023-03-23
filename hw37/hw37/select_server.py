#!/usr/bin/python3
import select
import socket

def handle(sock, addr):
    data = None
    try:
        data = sock.recv(1024) # Should be ready
    except ConnectionError:
        print(f"Client suddenly closed while receiving")
        return False
    print(f"Received {data} from: {addr}")
    if not data:
        print("Disconnected by", addr)
        return False
    number_one, oprtr, number_two = data.split()
    try:
        number_one, number_two = float(number_one), float(number_two)
        oprtr = oprtr.decode("utf-8")
    except: 
        pass
    try:
        operations = {
            "+": lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '/': lambda x, y: x / y,
            '*': lambda x, y: x * y,
            '**': lambda x, y: x ** y,
            '//': lambda x, y: x // y,
            '%': lambda x, y: x % y,
        }
        data = operations[oprtr](number_one, number_two)
    except: 
        pass
    print(f"Send: {data} to: {addr}")
    try:
        if not data:
            data = ""
        sock.send(str(data).encode()) # Hope it won't block
    except ConnectionError:
        print(f"Client suddenly closed, cannot send")
        return False
    return True


HOST, PORT = "", 9999
if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serv_sock:
        serv_sock.bind((HOST, PORT))
        serv_sock.listen(1)
        inputs = [serv_sock]
        outputs = []
        while True:
            print("Waiting for connections or data...")
            readable, writeable, exceptional = select.select(inputs, outputs, inputs)
            for sock in readable:
                if sock == serv_sock:
                    sock, addr = serv_sock.accept() # Should be ready
                    print("Connected by", addr)
                    inputs.append(sock)
                else:
                    addr = sock.getpeername()
                    if not handle(sock, addr):
                        # Disconnected
                        inputs.remove(sock)
                        if sock in outputs:
                            outputs.remove(sock)
                        sock.close()
                        