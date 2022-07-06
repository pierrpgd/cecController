import subprocess
import pexpect
import time

child = pexpect.spawn('cec-client -d 16')
child.expect('waiting for input')

while True:

	ordersString = ''

	with open('orders.txt') as orders:
		for order in orders:
			#print(order)
			ordersString = ordersString + order + ' '
			child.sendline(order)
			time.sleep(5)

	#print("requete du statut de la TV...")
	child.sendline('pow 0')
	info = child.expect(['power status: on', 'power status: standby', 'power status: unknown'])
	if info == 0:
		tvStatus = "on"
	elif info == 1:
		tvStatus = 'off'
	else:
		tvStatus = "unknown"
	time.sleep(5)
	#print("requete du statut de la barre son...")
	child.sendline('pow 5')
	info = child.expect(['power status: on', 'power status: standby', 'power status: unknown'])
	if info == 0:
		audioStatus = 'on'
	elif info == 1:
		audioStatus = 'off'
	else:
		audioStatus = "unknown"

	#print('tvStatus: ' + tvStatus + '\naudioStatus: ' + audioStatus)

	with open('tv_status.txt', 'w') as f:
		f.write(tvStatus)
	with open('audio_status.txt', 'w') as f:
		f.write(audioStatus)

	time.sleep(5)

	subprocess.Popen(["/home/pi/pythonScripts/transfert.sh"], shell=True)

	for n in range(0, len(ordersString.split(' ')), 2):
		if ordersString.split(' ')[n] == 'on' and ordersString.split(' ')[n+1] == '0' and tvStatus != 'on': continue
		if ordersString.split(' ')[n] == 'standby' and ordersString.split(' ')[n+1] == '0' and tvStatus == 'on': continue
		if ordersString.split(' ')[n] == 'on' and ordersString.split(' ')[n+1] == '5' and audioStatus != 'on': continue
		if ordersString.split(' ')[n] == 'standby' and ordersString.split(' ')[n+1] == '5' and audioStatus == 'on': continue

	if ordersString != '':
		with open('orders.txt', 'w') as f:
			f.write('')

child.sendline('q')
