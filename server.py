#!/usr/bin/python
#-*- coding: Utf-8 -*-

import socket, sys,os,signal,time

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
