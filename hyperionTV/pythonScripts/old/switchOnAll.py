import pexpect
import time

child = pexpect.spawn('cec-client -d 16')
print('appel de CEC...')
child.expect ('waiting for input')
print("requete du statut de la TV...")
child.sendline('pow 0')
info = child.expect(['power status: on', 'power status: standby', 'power status: unknown'])
if info == 0:
	print('TV est déjà allumée !')
elif info == 1:
	print('TV est éteinte !')
	print("demande d'allumer la TV...")
	child.sendline ('on 0')
	print('TV allumée !')
elif info == 2:
	print("impossible d'obtenir le statut de TV !")
time.sleep(2)
print("requete du statut de la barre son...")
child.sendline('pow 5')
info = child.expect(['power status: on', 'power status: standby', 'power status: unknown'])
if info == 0:
        print('barre son est déjà allumée !')
elif info == 1:
	print('barre son est éteinte !')
	print("demande d'allumer la barre son...")
	child.sendline('on 5')
	print("Barre de son allumée !")
elif info == 2:
        print("impossible d'obtenir le statut de barre son !")
print("fermeture de la connexion CEC.")

#short = 'power status: '
#retour_list = [short+'on',short+'standby',short+'unknown',pexpect.EOF,pexpect.TIMEOUT]
#retour = child.expect(retour_list)
#print(retour_list[retour])

child.sendline('q')
