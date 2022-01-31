import unittest
import switch

class TestSwitch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_ip = "10.10.10.10"
        cls.test_switch = ['i']
        cls.switch_test = switch.Switch('i', 'j', 'e', 'f')
    def test_fill_chosen_switches(self):
        self.switch_test.fill_chosen_switches(self.test_switch, i = self.test_ip)
        with self.assertRaises(switch.Switch):
            self.switch_test.fill_chosen_switches(['i'], i="10.10.10.10", e = "txt")
    def test_check_switches(self):
        self.assertEqual(self.switch_test.check_switches('i'), True)
        self.assertEqual(self.switch_test.check_switches('not valid'), False)
    def test_get_switch(self):
        self.assertEqual(self.switch_test.get_switch('i'), "10.10.10.10") 
        self.assertEqual(self.switch_test.get_switch('not valid'), "Please enter a valid switch")
