#!/bin/bash -x

'''

echo "test des paramètres du client"

./client.py 127.0.0.1

if [ $? == 0 ]; then
	echo "Il manque le numéro de port et le nom du client : Test 1 ECHEC"
fi

./client.py 127.0.0.1 5000

if [ $? == 0 ]; then
 	echo "Il manque le numéro le nom du client : Test 2 EHCEC"
fi

./client.py 127.0.0.1 5000 abdou

if [ $? == 0 ]; then
 	echo "Il manque le numéro le nom du client : Test 3 EHCEC"
else
     echo "Test des paramètres du client: OK"
fi
'''
