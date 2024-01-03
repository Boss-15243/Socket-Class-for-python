import socket
import sys

class Server:
    def __init__(self, ip, port):
        self.host_ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            self.socket.bind((self.host_ip,self.port))
        except PermissionError:
            print("Port couldn't be opened, please try another")
            sys.exit()
        self.connected = []
    
    def accept(self):
        conn, addr = self.socket.accept()
        self.connected.append((conn, addr))
        return (conn, addr)
    
    def listen(self,n):
        self.socket.listen(n)
    
    def send(self, data, conn):
        conn.send(data.encode())
    
    def sendall(self, data):
        for i in range(len(self.connected)):
            self.send(data, self.connected[i][0])
        
    def close(self):
        self.socket.close()

class Client:
    def __init__(self):
        self.socket = socket.socket()
    
    def connect(self, ip, port):
        self.socket.connect((ip, port))
        print("Connected succesfully")
    
    def recv(self):
        return self.socket.recv(1024).decode()