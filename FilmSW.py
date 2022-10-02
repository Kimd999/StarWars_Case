import collections
from itertools import count
from ActeurSW import *


class Film : 

    #Constructeur

    def __init__ (self, titre, annee_sortie, numero_ep, cout, recette, collection_acteurs) : 

        self.setTitre(titre)
        self.setAnnee(annee_sortie)
        self.setEp(numero_ep)
        self.setCout(cout)
        self.setRecette(recette)
        self.collection_acteurs = collection_acteurs

    #Création des setteurs

    def setTitre(self, titre) :
        self.titre = titre 
    
    def setAnnee(self, annee_sortie) : 
        self.annee_sortie = annee_sortie

    def setEp(self, numero_ep) : 
        self.numero_ep = numero_ep
    
    def setCout(self, cout) :
        self.cout = cout
    
    def setRecette(self, recette) : 
        self.recette = recette

    def setCollectionActeurs(self, collection_acteurs) :
        self.collection_acteurs = Acteur.__str__()
 


    #Création des getters 

    def getTitre(self) :
        return self.titre
    
    def getAnnee(self) : 
        return self.annee_sortie

    def getEp(self) : 
        return self.numero_ep
    
    def getCout(self) :
        return self.cout
    
    def getRecette(self) : 
        return self.recette
    
    def getCollectionActeurs(self) :
        return self.collection_acteurs

    #Fonction str 

    def __str__(self) :
        return str(self.titre) + " " + str(self.annee_sortie) + " " + str(self.numero_ep) + " " + str(self.cout) + " " + str(self.recette)

    #Fonction pour la question 11

    def nbActeur(self, collection_acteurs) :
       compteur = 0
       for nb_acteurs in collection_acteurs :
           compteur += 1
       return compteur 


 

    def calculBenefice(self, recette, cout) :
       return (recette - cout)

    

SW1 = Film('La Menace Fantôme', 1999, 'I', 115000000, 983600000)
SW2 = Film("L'Attaque des Clones", 2002, 'II', 115000000, 983600000)
SW3 = Film("La Revanche des Sith", 2005, 'III', 115000000, 983600000)

#SW4 = Film(titre = input("Veuillez entrer le titre : "), annee_sortie = input("Veuillez entrer l'année de sortie : "), numero_ep = input("Veuillez rentrer le numéro de l'épisode : "), cout = input("Veuillez rentrer le budget du film : "), recette = input("Veuillez rentrer la recette du film : "))

#print(SW1.__str__())
#print(SW4.__str__())

collection_films = [SW1,SW2, SW3]

def isBefore(self, annee) : 
   if annee > self.annee_sortie : 
       return True
   else : 
       return False 

def parcourirCollection(collection) :

    for films in collection : 
        print(films.__str__())



parcourirCollection(collection_films)
