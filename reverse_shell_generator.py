from pyconnection.connection import Connection
from switch import Switch
import os, sys
import re

def load_shell(file_name):
    try:
        with open(file_name, 'r'):
            return file_name.read()

    except FileNotFoundError as e:
        return False

    except:
        return False

def inject_shell(shell,ip,port):
    return shell.format(lhost=ip,lport=port)

# add automatic ip switch
def get_ip(interface):
    ip = Connection.get_ip_address(interface)
    return ip if ip else False


# add feature to scan directory for supported languages
SUPPORTEDLANGUAGES=os.listdir("shells")
#mark end of list
SUPPORTEDLANGUAGES.append("EOL")
#Script Switches
HELP=Switch('-h', func=lambda: print("python reverse_shell_generator.py language ip port"))
LANGUAGE=Switch('-l', regex=re.compile("^[a-z]+$"))
IP=Switch('-i', regex=Connection.IP_REGEX)
PORT=Switch('-p', regex=Connection.PORT_REGEX)
# convert all script switches to a list
SCRIPT_SWITCHES = Switch.switches_to_list(HELP, LANGUAGE, IP, PORT)

def main():
    # side project switch esc and caps
    # parse input to switches
    argv = Switch.parse_input(sys.argv)

    # used only positonal arguments
    if len(pos_argv) == 3:
        language = pos_argv[0]
        ip = pos_argv[1]
        port = pos_argv[2]

    # change to use the get_ip method by implementing switches
    # used optional arguments
    else:
        print("Feature needs to be implemented")
        sys.exit()


    # validate language command
    # get index of break
    for index, supported_language in enumerate(SUPPORTEDLANGUAGES):
        if language.get_value().lower() in supported_language.lower():
            break

    if supported_language == "EOL":
        print(f"Not a valid language. supported languages: (SUPPORTEDLANGUAGES)")
        sys.exit()

    # validate ip
    ip.set_regex(IP.get_regex())
    if not ip.has_valid_input():
        print("Incorrect IP Address")
        sys.exit()

    # validate port
    port.set_regex(PORT.get_regex())
    if not port.has_valid_input():
        print("Incorrect Port")
        sys.exit()

    # load shell
    raw_shell = load_shell(SUPPORTEDLANGUAGES[index])
    print(raw_shell)




    # create new shell














if __name__ == "__main__":
    main()
