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
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # crée un object socket
	server.bind((HOST,PORT)) #association host et du port
	server.listen(10)
	liste_de_connection.append(server)
	running = 1
	nb_client_conecte = 0 # nombre de client conecté

	while running:
		inputready,outputready,exceptready = select.select(liste_de_connection,[],[])
		for socket in inputready: #On a une nouvelle connection sur le serveur
			if socket == server:
				client, address = server.accept() # on accepte le client
				liste_de_connection.append(client) # on ajoute le nouveau client dans la liste des sockets
				nb_client_conecte =nb_client_conecte + 1 # Nouveau client vient d'arriver, on incremente
				print "Le client (%s, %s) est connecté" % address # permet de suivre les clients qui se connecte sur le serveur
			else:
				# On traite les messages reçu du client
				message = socket.recv(SIZE)
				try:
					print"test de l’envoi d’un message avec %d clients connectés: ok" % nb_client_conecte
					if message:
						envoie_message(socket, "\r" + message)                 
				except:
					envoie_message(socket, "Client (%s, %s) est hors ligne" % address)
					print "Le client (%s, %s) est hors ligne" % address
					nb_client_conecte =nb_client_conecte -1 # Un client est parti, on décremente
					socket.close()
					liste_de_connection.remove(socket)
					continue
	server.close()