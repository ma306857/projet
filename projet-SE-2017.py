#!/usr/bin/python
#-*- coding: Utf-8 -*-

import socket, sys,os,signal,time

print("A tout moment appuyé sur CTRL+C pour fermer le serveur, Merci :) ")

#création du fichier error.log
fichier_error = os.open("error.log", os.O_APPEND|os.O_CREAT|os.O_WRONLY) # créer le fichier et ajoute à la fin 

#création du fichier succes.log
fichier_succes = os.open("succes.log", os.O_APPEND|os.O_CREAT|os.O_WRONLY) # créer le fichier et ajoute à la fin 

def log_success(message):
    '''
    La fonction log succes permet d'ecrire un message de succès dans notre fichier succes.log
    '''
    os.write(fichier_succes, time.strftime("%A %d %B %Y %H:%M:%S") + " " + message + "\n")

def log_error(message):
    '''
    La fonction erreur succes permet d'ecrire un message de succès dans notre fichier error.log
    '''
    os.write(fichier_error, time.strftime("%A %d %B %Y %H:%M:%S") + " " + message + "\n")

print("A tout moment appuyé sur CTRL+C pour fermer le serveur, Merci ! ")

#création du fichier succes.log
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
    os.close(fichier_succes) #fermeture du fichier succes.log
    os.close(fichier_error)#fermeture du fichier error.log
    os.close(historique_activite) #fermeture du fichier succes.log
    server.close()

#ici on souhaite attraper le signal CTRL C à l'aide du traitant
signal.signal(signgit al.SIGINT, traitant)


'''
        PARTIE PRINCIPAL DU CLIENT 
'''

