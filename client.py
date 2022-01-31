import socket


class Client:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.connect((host, port))
        self.ip = self.sock.getsockname()[0]

    def stop(self):
        self.sock.close()

    
