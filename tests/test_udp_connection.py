import socket
import unittest
from connection_tools import udp_connection

class TestUDPConnection(unittest.TestCase):
    @classmethod
    def setUp(cls):
       cls.ip = "8.8.8.8"
       cls.port = 80
       cls.udp_connection = udp_connection.UDPConnection(cls.ip, cls.port)
    @classmethod
    def tearDown(cls):
        cls.udp_connection.stop()
    def test_get_ip(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect((self.ip, self.port))
        client_ip = sock.getsockname()[0]
        sock.close()
        self.assertEqual(self.udp_connection.get_ip(),client_ip)
