#!/bin/bash -x

echo "Test de deconnection d’un client: ok "

gnome-terminal -e ./server.py 5000 8080 # on lance sur le serveur

gnome-terminal -e ./client.py localhost 5000 David 

pid=$(ps aux | grep 'client.py' | awk '{print $2}') # tuer le client

pkill -9 $pid

if [[ $? -eq 0 ]]
then
	echo "Test de deconnection d’un client : reussi"
else
	echo "Test de deconnection d’un client : échoué "
fi