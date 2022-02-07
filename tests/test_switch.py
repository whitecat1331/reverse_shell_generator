import unittest
from script_tools import switch
from exceptions import exceptions

class TestSwitch(unittest.TestCase):
    def setUp(self):
        self.test_switch = switch.Switch("i", required = True, value="0.0.0.0", execution=(lambda: "This is a test"))
        self.test_value = "10.10.10.10"


    def test_set_value(self):
        self.test_switch.set_value(self.test_value)
        self.assertEqual(self.test_switch.get_value(), self.test_value)

    def test_get_value(self):
        self.assertEqual(self.test_switch.get_value(), "0.0.0.0")
        with self.assertRaises(exceptions.Switch_Value_Error):
            switch_exeception = switch.Switch("a", True)
            switch_exeception.get_value()

    def test_execute(self):
        self.assertEqual(self.test_switch.execute()(), "This is a test")

    def test_bool(self):
        self.assertEqual(bool(self.test_switch), True)

