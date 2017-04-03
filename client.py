#!/usr/bin/python
#-*- coding: Utf-8 -*-
import socket, sys,os,signal,time,select

# faire attention a la primitive #ACCEPT car elle est BLOQUANTE (cf cours)
'''
		COTE CLIENT 
'''
print("Pour quitter le chat CTRL+C ")

def handler(sig,frame):
	print"Signal SIGINT recu fermeture du client"
	sock.close()
	server.close()
	sys.exit(0)
#ici on souhaite attraper le signal CTRL C à l'aide du traitant
signal.signal(signal.SIGINT, handler)

def envoie_message (sock, message):
	# Cette fonction me permet d'envoyer des messages entre les clients 
	for socket in liste_de_connection:
		if socket != server:
			# on eassaye d'envoyer le message
			try :
				socket.send(message)
			except :
				# on ferme la connection et on supprime des clients des connections
				socket.close()
				liste_de_connection.remove(socket)

if __name__ == "__main__":

	# nombre des arguments est insuffisant
	if(len(sys.argv) < 4):
		print "Test du nombre d'argument coté client a échoué, dans l'ordre : IP_CLIENT, PORT_CLIENT, NOM_CLIENT "
		sys.exit()

	print "Test nombre d'argument client: OK"
	liste_de_connection = []
	SIZE = 4096
	ip_client = str((sys.argv[1])) # on rentre le numéro de l'ip  : '127.0.0.1'
	port_client = int(sys.argv[2]) # on rentre le numéro de port
	nom_client =  str((sys.argv[3])) # nom du nouveau client qui sait connecter
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	running = 1

	# Tentative de connection
	try :
		server.connect((ip_client, port_client))
		print 'Connexion avec le serveur établie : OK'
	except :
		print 'Connexion échoué avec le serveur'
		sys.exit()

	while running:
		liste_de_connection = [sys.stdin,server]
		inputready,outputready,exceptready = select.select(liste_de_connection,[],[])
		for sock in inputready:
			if sock == server:
				# On traite les messages reçu du serveur
				message = sock.recv(SIZE)
				if not message :
					print '\n Le serveur est deconnecté '
					sys.exit()
				else :
					#affichier le message rçu par le serveur
					sys.stdout.write(message)
			else :
				# j'envoie un message 
				msg = sys.stdin.readline()
				server.send(nom_client +" : " + msg) #nom_client pour afficher le nom au début
	server.close()

