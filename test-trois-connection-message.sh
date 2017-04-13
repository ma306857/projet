#!/bin/bash 

echo "Test de l’envoi d’un message avec 3 clients connectés"

gnome-terminal -e ./server.py 5000 8080 & # on lance sur le serveur

gnome-terminal -e nc localhost 5000 & # premier client
gnome-terminal -e nc localhost 5000 & # deuxième client

nc localhost 5000  | echo "toto"  > result-with-three-client # troisième client et on un envoie un message

echo  "toto" > expected-with-three-client

diff result-with-three-client expected-with-three-client

if [[ $? -eq 0 ]]
then
	echo "Test de l’envoi d’un message avec 3 clients connectés : reussi"
else
	echo "Test de l’envoi d’un message avec 3 clients connectés : échoué"
fi

pid=$(ps aux | grep 'server.py' | awk '{print $2}') # tuer le serveur
kill $pid # on tue le processus 
