import unittest
from script_tools import script_manager

class TestScriptManager(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.script_arguments = "-a -o shell.sh -p 00"

    def test_is_switch(self):
        self.assertEqual(script_manager.is_switch("-a"), True)
        self.assertEqual(script_manager.is_switch("shell.sh"), False)


