import pexpect
import time

child = pexpect.spawn('cec-client -d 16')
print('appel de CEC...')
child.expect ('waiting for input')
print("requete du statut de la TV...")
child.sendline('pow 0')
info = child.expect(['power status: standby', 'power status: on', 'power status: unknown'])
if info == 0:
	print('TV est déjà éteinte !')
elif info == 1:
	print('TV est allumée !')
	print("demande d'éteindre la TV...")
	child.sendline ('standby 0')
	print('TV éteinte !')
elif info == 2:
	print("impossible d'obtenir le statut de TV !")
time.sleep(2)
print("requete du statut de la barre son...")
child.sendline('pow 5')
info = child.expect(['power status: standby', 'power status: on', 'power status: unknown'])
if info == 0:
        print('barre son est déjà éteinte !')
elif info == 1:
	print('barre son est allumée !')
	print("demande d'éteinte la barre son...")
	child.sendline('standby 5')
	print("Barre de son éteinte !")
elif info == 2:
        print("impossible d'obtenir le statut de barre son !")
print("fermeture de la connexion CEC.")

#short = 'power status: '
#retour_list = [short+'on',short+'standby',short+'unknown',pexpect.EOF,pexpect.TIMEOUT]
#retour = child.expect(retour_list)
#print(retour_list[retour])

child.sendline('q')
