import socket
import threading


class UDPConnection:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.connect((host, port))

    def stop(self):
        self.sock.close()

    def get_ip(self):
        return self.sock.getsockname()[0]

