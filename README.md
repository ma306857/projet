# projet-SE

Client-Serveur IRC

Le but du projet cette année est la réalisation d’un serveur IRC.
Le projet est à réaliser en binôme. Les binômes devront être annoncés à l’enseignant chargé de TD lors de la séance de TD de la semaine 10
1. Contrat minimal (10 points)

Pour avoir la moyenne, vous devrez fournir le code d’un serveur et d’un client écrit en python. Votre code doit être original et n’utiliser que les primitives que nous avons vues en cours.
1.1 Client

Le client doit accepter trois arguments sur la ligne de commande:
le nom (ou l’ip) du serveur
le numero de port sur lequel se connecter au serveur
l’identifiant de l’utilisateur
Exemple:
   $ client nil.unice.fr 4200 olivier
Le client minimal doit se connecter au serveur, lui transmettre l’identifiant et se mettre en attente des événements suivants:
Saisie de l’utilisateur au clavier: le texte saisi est envoyé au serveur
Reception d’un message du serveur: le message est affiché sur la sortie standard
Terminaison par Ctrl-C ou Ctrl-D
1.2 Serveur

Le serveur accepte seulement un argument sur la ligne de commande: le numero de port sur lequel il reçoit les connections du client:
   $ server 4200
Une fois qu’il a démarré, le serveur minimal se met en attente des événements suivants:
réception d’une demande de connexion: le serveur accepte la connexion et ajoute le socket du client a sa liste des clients connectés
réception d’un message d’un client: le serveur reçoit le message puis le renvoie à tous les clients connectés
Déconnexion d’un client: retrait du socket de la liste des clients connectés
Lorsqu’il retourne les messages vers les clients, le serveur doit ajouter l’identifiant de l’utilisateur du client au debut de chaque ligne de message.
Par exemple, si deux clients, grosso et modo sont connectés, et que grosso envoie le message hello, on voit s’afficher la ligne suivante sur la sortie standard du client:
  $ client nil.unice.fr 4200 grosso
  hello
  grosso: hello


  $ client nil.unice.fr 4200 modo
  grosso: hello
1.3 Tests

Les tests sont très importants. Ils vous permettent de vérifier que toutes les fonctionnalités de votre systèmes sont implémentées sans erreur.
Les commandes telnet et nc (netcat) vous seront très utiles pour simuler l’une ou l’autre des parties:
pour simuler le serveur quand vous souhaitez tester le client
pour simuler le client quand vous souhaitez tester le serveur
Telnet s’utilise essentiellement de façon interactive, mais netcat permet aussi un fonctionnement en mode batch, qui est parfait pour écrire un script.
La commande xterm peut être lancées de façon à exécuter une commande à de façon automatique à l’aide de l’option -e.
Par exemple la commande suivante ouvre un xterm et lui fait exécuter la commande cat /etc/passwd > /tmp/toto. Losrque la commande est terminée, le xterm se ferme automatiquement.
Vous pouvez donc utiliser cette commande pour lancer automatiquement un plusieurs client, chacun dans un xterm différent. Vous pouvez aussi lancer des scripts qui exécutent plusieurs commandes (par exemple netcat) dans un xterm, sans avoir a retaper à chaque fois les même commandes.
2 Bonus

2.1 Bonus Tests (4 points)

Ecrivez des scripts qui testent de facon automatique le bon fonctionnement de chacune des fonctions du client et du serveur. Vos tests doivent couvrir un maximum de situations différentes: arrivées consécutives de clients, départs de clients, etc. Pour chaque test vous devrez produire une sortie qui affiche le nom du test et un message indiquant si le test est réussi.
Par exemple:
test des paramètres du client: ok
test de connection et envoi d’un message par un client: ok
test de l’envoi d’un message avec 3 clients connectés: ok
test de trois connections simultanées au serveur: ok
test de trois réceptions simulatanées depuis 3 clients différents: ok
test de deconnection d’un client: ok
…
2.2 Bonus Interface Web (5 points)

Le serveur accepte un deuxième numéro de port en paramètre. Ce numéro de port fourni un service de mini serveur web, qui renvoie un page html contenant une liste des 5 derniers messages reçus (et renvoyés) par le serveur.
Le contenu de cette page est minimal: chaque message sera présenté sous la forme d’un item (li) dans une liste.
2.3 Tests sur le bonus 2.2 (2 points)
