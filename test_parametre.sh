#!/bin/bash -x

echo "Test des paramètres du client"

nc -l 5000&

./client.py 127.0.0.1

if [ $? != 0 ]; then
	echo "Il manque le numéro de port et le nom du client : Test 1 ECHEC"
fi

./client.py 127.0.0.1 5000

if [ $? != 0 ]; then
 	echo "Il manque le numéro le nom du client : Test 2 EHCEC"
fi

./client.py 127.0.0.1 5000 abdou&

if [ $? -eq 0 ]; then
     echo "Test des paramètres du client: OK"
else
 	echo "Un soucis quelque part : Test 3 EHCEC"
fi