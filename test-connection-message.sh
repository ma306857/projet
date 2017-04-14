#!/bin/bash -x

echo "Test de connection et envoi d’un message par un client"

gnome-terminal -e ./server.py 5000 8080 # on lance le serveur 

nc localhost 5000  | echo "toto"  > result-with-on-client # on connecte un client et on envoie un message 

echo  "toto" > expected-with-on-client # on sauvegarde le resultat attendu

diff result-with-on-client expected-with-on-client # on compare les deux fichiers

if [[ $? -eq 0 ]]
then
	echo "Test de connnection et envoi d'un message par un client : reussi "
else
	echo "Test de connnection et envoi d'un message par un client : échoué"
fi

pid=$(ps aux | grep 'server.py' | awk '{print $2}') # récupere le pid du processus 
kill $pid # on tue le processus 
