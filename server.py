#!/usr/bin/python
#-*- coding: Utf-8 -*-

import socket,sys,os,signal,time,select
from collections import deque
# faire attention a la primitive #ACCEPT car elle est BLOQUANTE (cf cours)
'''
		COTE SERVEUR 
'''

def envoie_message (sock, message):
	# Cette fonction me permet d'envoyer des messages entre les clients 
	for socket in liste_global:
		if socket != irc_sock and socket != web_sock:
			# on eassaye d'envoyer le message
			try :
				socket.send(message)
			except :
				# on ferme la connection et on supprime le client de la liste des connections
				socket.close()
				liste_de_connection.remove(socket)

# j'ai besoin de la variable à plusieurs de mon programme, il faut garder les valeurs du tableau_content
global tableau_content
tableau_content = deque(["","","","",""])

def sauvegarde_conversation(message): 
	'''
	Garde les cinq derniers conversations dans une liste
	'''
	if len(tableau_content) == 5 :
		tableau_content.append(message)
		tableau_content.popleft()
		return tableau_content
	
if __name__ == "__main__":
	# nombre des arguments est insuffisant
	if(len(sys.argv) < 2) :
		print 'Argument manquant : indiquer le numéro de PORT '
		sys.exit()

	print "Test argument serveur : OK"
	liste_de_connection = [] # constitue la liste des sockets qui vont se connecter
	SIZE = 4096
	
	HOST = '127.0.0.1' #localhost
	
	PORT = int(sys.argv[1]) #int par ce que sys.argv[] rend un str, Ici on rentre le numéro du port
	PORT_NAVIGATEUR = int(sys.argv[2]) #int par ce que sys.argv[] rend un str, Ici on rentre le numéro du port du navigateur
	
	irc_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # crée un object socket pour le client
	web_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # crée un object socket pour le navigateur	
	
	irc_sock.bind((HOST,PORT)) #association host et du port client
	web_sock.bind((HOST,PORT_NAVIGATEUR)) #association host et du port navigateur

	irc_sock.listen(10)
	web_sock.listen(10)

	liste_global = [irc_sock,web_sock] # liste qui contient l'ensemble des sockets IRC + WEB
	liste_irc = [] # liste qui contient les sockets IRC 
	liste_web = [] # liste qui contient les sockets WEB
	running = 1

	while running:
		inputready,outputready,exceptready = select.select(liste_global,[],[])
		for socket in inputready: #On a une nouvelle connection sur le serveur

			if socket == irc_sock:
				client, address = irc_sock.accept() # on accepte le client
				liste_global.append(client) # on ajoute le nouveau client dans la liste des sockets
				liste_irc.append(client) # on ajoute le client dans la liste IRC
				print "Le client (%s, %s) est connecté" % address # permet de suivre les clients qui se connecte sur le serveur

			elif socket == web_sock :
				navigateur, address = web_sock.accept() # on accepte le navigateur
				liste_global.append(navigateur) # on ajoute le nouveau client dans la liste des sockets
				liste_web.append(navigateur) # on ajoute le client dans la liste WEB
				print "Le client (%s, %s) est connecté" % address # permet de suivre les clients qui se connecte sur le serveur

			# C'est une socket de type client_IRC
			elif socket in liste_irc:
				# On traite les messages reçu du client
				message = socket.recv(SIZE)
				sauvegarde_conversation(message) # on sauvegarde ce que je reçois
				if not message:
					envoie_message(socket, "Client (%s, %s) est hors ligne\n" % address)
					liste_global.remove(socket) # on supprime le socket dans la liste global
					liste_irc.remove(socket) # on supprime le socket dans la liste_IRC
					socket.close()
				else:
					envoie_message(socket, "\r" + message)
					sauvegarde_conversation(message) #on sauvegarde ce que j'envoie

			else:
				preparation_message = list(tableau_content)
				cinq_message = [w.replace('\n', '') for w in preparation_message] # on enlève les backslashs dans la liste, produit par ENTER quand le client envoie un message
				content = "<html> <head> </head> <body>  <li> " + cinq_message[0] + " </li> <li> "+ cinq_message[1]+ "</li> <li>"+ cinq_message[2]+" </li> \
				<li> " + cinq_message[3] + "</li> <li> "+ cinq_message[4]+ "</li>  </body> </html>"

				content_length = len(content)
				entetes = 'HTTP/1.1 200 OK\nDate : ' + time.strftime("%A %d %B %Y %H:%M:%S") + '\nContent-type: text/html\ncontent_length : '+ str(content_length)+'\n\n' # préparation des entetes
				socket.send(entetes) # Envoie des entetes
				socket.send(content) # Envoie envoie du message principal
				liste_global.remove(socket)
				liste_web.remove(socket)
				socket.shutdown(1)

	web_sock.close()
	irc_sock.close()