# cecController
Programme de contrôle d'une TV et d'une barre audio à travers HDMI-CEC

Fonctionnement avec 2 Raspberry :
- HYPERIONTV est connectée à la TV par HDMI et envoie les commandes CEC aux périphériques connectés par HDMI.
- HASSIO est le serveur domotique Home Assistant qui envoie les ordres de commande à HyperionTV et reçoit les statuts des périphériques TV.

Répertoire HYPERIONTV contient les scripts de commande, de contrôle du statut des périphériques et le script Bash de transmission des statuts au HASSIO.
Répertoire HASSIO contient les fichiers de statut des périphériques TV. Les ordres de commandes sont envoyés par SSH à HYPERIONTV.