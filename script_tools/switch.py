from exceptions import exceptions

class Switch():
    def __init__(self, char, required = False, value = None, execution = None):
        self.char = char
        self.required = required
        self.value = value
        self.execution = execution

    def set_value(self, value):
        self.value = value

    def execute(self):
        return self.execution

    def get_value(self):
        if(self.value != None):
            return self.value
        else:
            raise exceptions.Switch_Value_Error()

    def __bool__(self):
        return self.required

