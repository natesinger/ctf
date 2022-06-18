#https://docs.pwntools.com/en/stable/
#https://readthedocs.org/projects/pwntools/downloads/pdf/beta/
import socket, paramiko
from pwn import *

TARGET_HOST = 'localhost'
TARGET_PORT = 22
TARGET_USER = 'username'
TARGET_PASSWORD = 'pasword'

# For easy coloring options
class ANSI:
    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKCYAN    = '\033[96m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    ENDC      = '\033[0m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'

# Make connection to target SSH and save as pwntubes object in io
try: io = process(f"sshpass -p {TARGET_PASSWORD} ssh -oStrictHostKeyChecking=no {TARGET_USER}@{TARGET_HOST} -p{TARGET_PORT}", shell=True)
except socket.gaierror as e:
    print(f"{ANSI.FAIL}Socket Error: Name resolution failure ({type(e)}){ANSI.ENDC}"); exit()
except pwnlib.exception.PwnlibException as e:
    print(f"{ANSI.FAIL}Socket Error: Could not connect to target ({type(e)}){ANSI.ENDC}"); exit()
except paramiko.ssh_exception.AuthenticationException as e:
    print(f"{ANSI.FAIL}Socket Error: Could not authenticate ({type(e)}){ANSI.ENDC}"); exit()
except Exception as e:
    print(f"{ANSI.WARNING}Socket Error: Unknown error occured ({type(e)}:{e}){ANSI.ENDC}")

""" RECEIEVE METHOD REFERENCE... more at https://docs.pwntools.com/en/stable/tubes.html
-- Recieve Number of Bytes --
io.recv(numb = 4096, timeout = default) → bytes... https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.recv

-- Recieve until EOF --
recvall() → bytes... https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.recvall
    There is also recvallS and recvallB for string or byte returns

-- Recieve a line --
recvline(keepends=True, timeout=default) → bytes... https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.recvline
    There is also recvlineS for a string return

-- Recieve x number of lines --
recvlines(numlines, keepends=False, timeout=default) → list of bytes objects... https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.recvlines
    There is also recvlinesS and recvlinesB for string or byte returns

-- Recieve until a specific byte arrary is recognized --
recvuntil(delims, drop=False, timeout=default) → bytes... https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.recvuntil
    There is also recvuntilS and recvuntilB for string or byte return

-- Recieve until a line contains x --
recvline_contains(items, keepends=False, timeout=pwnlib.timeout.Timeout.default)... https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.recvline_contains
    There is also recvline_containsS and recvline_containsb for string or byte returns
    There is also recvline_endswith for if a line ends with one of x delimteres
    There is also recvline_startswith for if a line ends with one of x delimteres
        There are also byte and string versions of each of these"""


"""SEND METHOD REFERENCE... more at https://docs.pwntools.com/en/stable/tubes.html
-- Send data to a tube --
send(data)... https://docs.pwntools.com/en/stable/tubes.html

-- Send data after receiving something --
sendafter(delim, data, timeout = default)... https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.sendafter

-- Send a line of data, with LF/CRLF --
sendline(data)... https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.send
    Defaults to LF, can set CRLF with tube.newline = b"\r\n"

-- Send a line of data after receiving something --
sendlineafter(delim, data, timeout = default) → str...https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.sendlineafter
"""
# Do all the CTF things here




# Make the shell interactive if you want, useful to easily print flags if unpredictable
io.interactive()