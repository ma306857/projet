#!/usr/bin/env zsh

echo "test des paramètres du client"

re='^[0-9]+$'
 echo " "
 echo "Parametre 1: $1"
 if ! [[ $1 =~ $re ]]; then
    exit 3
 fi

 echo " "
 echo "paramètre 2: $2"
 if ! [[ $2 =~ $re ]]; then
    echo "Rentrer le numéro de port."
    exit 2
 fi

 re='^[[:graph:]]+$'
 echo " "
 echo "paramètre 3: $3"
 if ! [[ $3 =~ $re ]]; then
    echo "Entrer votre prénom ."
    exit 3
 fi
 echo " "
 ./client.py $1 $2 $3
 echo " "