#!/usr/bin/python
#-*- coding: Utf-8 -*-

import socket,sys,os,signal,time,select
# faire attention a la primitive #ACCEPT car elle est BLOQUANTE (cf cours)

'''
		COTE SERVEUR 
'''

def envoie_message (sock, message):
	# Cette fonction me permet d'envoyer des messages entre les clients 
	for socket in liste_de_connection:
		if socket != server:
			# on eassaye d'envoyer le message
			try :
				socket.send(message)
			except :
				# on ferme la connection et on supprime le client de la liste des connections
				socket.close()
				liste_de_connection.remove(socket)

if __name__ == "__main__":
	# nombre des arguments est insuffisant
	if(len(sys.argv) < 2) :
		print 'Argument manquant : indiquer le numéro de PORT '
		sys.exit()

	print "Test argument serveur : OK"
	liste_de_connection = [] # constitue la liste des sockets qui vont se connecter
	SIZE = 4096
	HOST = '127.0.0.1'
	PORT = int(sys.argv[1]) #int par ce que sys.argv[] rend un str, Ici on rentre le numéro du port
	irc_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # crée un object socket
	irc_sock.bind((HOST,PORT)) #association host et du port
	irc_sock.listen(10)
	liste_de_connection = [irc_sock]
	running = 1

	while running:
		inputready,outputready,exceptready = select.select(liste_de_connection,[],[])
		for socket in inputready: #On a une nouvelle connection sur le serveur
			if socket == irc_sock:
				client, address = irc_sock.accept() # on accepte le client
				liste_de_connection.append(client) # on ajoute le nouveau client dans la liste des sockets
				print "Le client (%s, %s) est connecté" % address # permet de suivre les clients qui se connecte sur le serveur
			else:
				# On traite les messages reçu du client
				message = socket.recv(SIZE)
				if not message:
					envoie_message(socket, "Client (%s, %s) est hors ligne" % address)
					print "Le client (%s, %s) est hors ligne" % address
					socket.close()
					liste_de_connection.remove(socket)
				else:
					envoie_message(socket, "\r" + message)                 
					continue
	irc_sock.close()