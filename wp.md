# Ice_bag ’s Write up for makerctf2019
## 1.easy_heap
漏洞：fastbin单向链表，free函数可重复free同一个chunk。
利用方式：
free chunk_a后free chunk_b（chunk_a,chunk_b,size相同），再次free chuk_a,即可骗过重复free的检测。
由fastbin的工作机制可知，我们创建了一个环形链表。又因为fastbin 遵循先入后出的机制，所以此时fastbin中未利用的chunk 为：chunk_a-->chunk_b-->chunk_a。
这时我们申请一个size相同的chunk即分配到chunk_a并能够对chunk_a 内容进行编辑（伪造chunk）前8个字节为伪造的fd，再次申请相同size的chunk，我们分配到chunk_b，随便写些什么在里面，再次申请相同size的chunk ，根据fastbin链表chunk_b-->chunk_a，我们分配到了chunk_a（实际上已经分配并伪造过了），随便写些东西在里面，再次申请相同size的chunk，即可分配到伪造fd对应地址的一块内存并对其任意修改。
## 2.SSP
  Checksec后发现开了canary栈保护，我们利用gets栈溢出漏洞时会被检测到，程序自动退出。输出为arg[0]，搜索字符串，发现存在字符串”flag{****i am on the server****}”
  这应该就是flag了只不过在远端的服务器上，所以只要将flag的地址覆盖到arg[0]输出错误信息时就会把flag交出来。
## 3.easy_rop
漏洞：main ida f5发现read(0,buff,0x200ull)存在输入溢出。
利用：
利用libc中的write函数泄露libc加载的基址，再找到system和/bin/sh
使用pwntools中的ROPgadgets找到能够传入参数的语句
发送payload get shell
