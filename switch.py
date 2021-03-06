import re


class Switch:

    def __init__(self, symbol, value=None,func=None,required=False,regex=None):
        self.symbol=symbol
        self.required=required
        self.value=value
        self.func=func if func else lambda: None
        try:
            self.regex = re.compile(regex) if regex else None
        except:
            self.regex = None

    def is_required(self):
        return self.required

    def get_value(self):
        return self.value

    def get_func(self):
        return self.func

    def set_regex(self,regex):
        self.regex=regex

    def get_regex(self):
        return self.regex

    def get_symbol(self):
        return self.symbol

    def has_valid_input(self):
        try:
            return re.fullmatch(self.regex,self.value) if self.regex else False

        except:
            return False


    def set_script_switches(self, *args):
        self.script_switches = []
        for arg in args:
            self.script_switches.append(arg)


    # convert input into list of switches
    # fill script switches with input values
    @classmethod
    def parse_input(cls, system_arguments):
        argument_iter = iter(system_arguments)
        input_switches = []
        for argument in argument_iter:
            if '-' in argument:
                input_switches.append(cls(argument, next(argument_iter, None)))
            else:
                positional_arguments.append(cls(argument_iter))

        return input_switches

    # set value from the input switches to the script switches
    @classmethod
    def parse_switches(cls, input_switches):
        for input_switch in input_switches:
            if input_switch.get_symbol in


    @staticmethod
    def switches_to_list(*args):
        script_list = []
        for arg in args:
            script_list.append(arg)

        return script_list

    @staticmethod
    def validate_all_switches(switches):
        all_valid = True
        for switch in switches:
            all_valid = switch.has_valid_input() and all_valid

        return all_valid

