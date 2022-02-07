def process_input(script_arguments):
    #convert list to dictionary if the next argument is not a switch
    return {script_arguments[i]: script_arguments[i+1] for i in range(len(script_arguments)) if not is_switch(script_aruguments[i+1])}

def is_switch(argument):
    return "-" in argument

def process_auto_switches(script_arguments):
    return [script_arguments[i] for i in range(len(script_arguments)) if is_switch(script_arguments[i+1])]
