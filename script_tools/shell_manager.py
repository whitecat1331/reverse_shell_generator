import os
from exceptions import exceptions

def load_shell(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().strip()

def inject(raw_shell, ip, port):
    return raw_shell.format(lhost=ip, lport=port)

def generate_shell(file_path, shell):
    with open(file_path, 'w', encoding='utf-8') as f:
            f.write(shell)
            os.chmod(file_path, 0o700)

