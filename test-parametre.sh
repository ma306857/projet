#!/bin/bash

echo "Test des paramètres du client"

gnome-terminal -e nc -l 5000 & # on lance le serveur avec netcat

./client.py 127.0.0.1 # on oublie le port et le nom du client

if [ $? != 0 ]; then
	echo "Test des paramètres du client : échoué (manque n° de port et nom client) "
fi

./client.py 127.0.0.1 5000 # on oublie le numéro de port et le nom du client

if [ $? != 0 ]; then
 	echo "Test des paramètres du client : échoué (manque n° de port et nom client) "
fi

gnome-terminal -e ./client.py 127.0.0.1 5000 abdou & # commande avec les bons paramètres

if [ $? -eq 0 ]; then
     echo "Test des paramètres du client: reussi"
else
 	echo "Test des paramètres du client : échoué (manque n° de port et nom client) "
fi

pid=$(ps aux | grep 'nc' | awk '{print $2}') # récupere le pid du processus 
kill $pid # on tue le processus
