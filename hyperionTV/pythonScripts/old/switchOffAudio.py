import pexpect

child = pexpect.spawn('cec-client -d 16')
child.expect ('waiting for input')
child.sendline('pow 5')
info = child.expect(['power status: on'])
print(info)
if info == 0:
	child.sendline ('standby 5') 
child.sendline('q')
