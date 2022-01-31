class Switch(Exception):
    def __init__(self, *args):
        self.switches = [*args]

    def fill_chosen_switches(self, chosen_switches, **kwargs):
      if len(chosen_switches) == len(kwargs):
        self.switches_chosen = { chosen_switches[i]: kwargs[chosen_switches[i]] for i in range(len(chosen_switches))}
      else:
        raise Switch("Chosen switches and values do not match")

    def check_switches(self, switch):
        return switch in self.switches
    def get_switch(self, switch):
        return self.switches_chosen.get(switch, "Please enter a valid switch")

