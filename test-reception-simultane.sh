#!/bin/bash 

echo "Test de trois réceptions simulatanées depuis 3 clients différents"

gnome-terminal -e ./server.py 5000 8080 & # on lance sur le serveur

client1="$(gnome-terminal -e nc localhost 5000)"
client2="$(gnome-terminal -e nc localhost 5000)"

nc localhost 5000  | echo "fleur" # troisième client connecté sur le serveur

echo  "fleur" > expected-reception

echo $client1

diff expected-reception recu1 recu2

if [[ $? -eq 0 ]]
then
	echo "Test de trois connections simultanées au serveur : reussi"
else
	echo "test de trois connections simultanées au serveur : échoué"
fi

pid=$(ps aux | grep 'server.py' | awk '{print $2}') # tuer le serveur
kill $pid # on tue le processus 
