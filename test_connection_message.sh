#!/bin/zsh

echo "Test de connection et envoi d’un message par un client"

./server.py 5000 8080 & 

echo "toto" | nc localhost 5000 > resultat

echo  "toto" > expected

diff resultat expected

if [[ $? -eq 0 ]]
then
	echo "Test reussi : ok"
else
	echo "Un truc cloche"
fi

# retrouver pid du serveur

pid=$(ps aux | grep ‘server.py' | awk '{print $2}’) 
# tuer le serveur
kill $pid