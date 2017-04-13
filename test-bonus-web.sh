#!/bin/bash  -x
echo "Test bonus web"

gnome-terminal -e ./server.py 5000 8080 & # on lance sur le serveur

gnome-terminal -e ./client.py localhost 5000 jacqueline | echo "j'aime le printemps"

wget localhost:8080 > index.html
 
diff execpt-bonus-web index.html

if [[ $? -eq 0 ]]
then
	echo "Test bonus web: reussi"
else
	echo "Test bonus web : échoué"
fi

pid=$(ps aux | grep 'server.py' | awk '{print $2}') # tuer le serveur
pkill $pid # on tue le processus 
