#!/usr/bin/python
#-*- coding: Utf-8 -*-

import socket, sys,os,signal,time

print("A tout moment appuyé sur CTRL+C pour fermer le serveur, Merci :) ")

#création du fichier historique_activite.log
historique_activite = os.open("historique_activite.log", os.O_APPEND|os.O_CREAT|os.O_WRONLY) # créer le fichier et ajoute à la fin 

def log_historique(message):
    '''
    La fonction log succes permet d'ecrire un message de succès dans notre fichier succes.log
    '''
    os.write(historique_activite, time.strftime("%A %d %B %Y %H:%M:%S") + " " + message + "\n")

# Le traitant
def traitant(signal, frame):
    '''
    Le traitant permet de cloturer notre serveur avec CTRL+C
    '''
    os.close(historique_activite) #fermeture du fichier succes.log
    server.close()

#ici on souhaite attraper le signal CTRL C à l'aide du traitant
signal.signal(signal.SIGINT, traitant)


'''
        PARTIE PRINCIPAL DU CLIENT 
'''


'''
        PARTIE DU SERVEUR 
'''
liste_de_connection = [] # constitue la liste des sockets qui vont se connecter
size = 4096
host = '127.0.0.1'
port =   int(sys.argv[1]) #int par ce que sys.argv[] rend un str, Ici on rentre le numéro du port
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # crée un object socket
server.bind((host,port)) #association host et du port
server.listen(10)
liste_de_connection.append(server)
running = 1


while running:
        inputready,outputready,exceptready = select.select(liste_de_connection,[],[])
        for s in inputready:
            #On a une nouvelle connection sur le serveur
            if s == server_socket:
                client, address = server_socket.accept()
                liste_de_connection.append(client) # on ajoute le nouveau client dans la liste des sockets
                print "Le client (%s, %s) est conecté" % address
server_socket.close()
