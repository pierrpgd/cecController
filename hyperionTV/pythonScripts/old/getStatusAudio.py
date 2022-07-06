import pexpect
import time

child = pexpect.spawn('cec-client -d 16')
child.expect ('waiting for input')
child.sendline('pow 5')
info = child.expect(['power status: on', 'power status: standby', 'power status: unknown'])
if info == 0:
	print('on')
elif info == 1:
	print('off')
elif info == 2:
	print("unknown")

child.sendline('q')
