#class pour créer les acteurs
from xml.dom import NO_MODIFICATION_ALLOWED_ERR
from PersoSW import *

class Acteur : 

    def __init__(self, nom, prenom, personnage) :
        self.setNom(nom)
        self.setPrenom(prenom)
        self.personnage = personnage

    #setters 

    def setNom(self, nom) : 
        self.nom = nom 
    
    def setPrenom(self, prenom) : 
        self.prenom = prenom 
    
    def setPersonnage(self, personnage) :
        #self.personnage = (Personnage.__str__())
        self.personnage = ()
        self.personnage.append(Personnage.__str__())

    #getters 
    
    def getNom(self) :
        return self.nom

    def getPrenom(self) : 
        return self.prenom
    
    def getPersonnage(self) :
        return self.personnage
    
    #fonction pour parcourir le tuple contenant les personnages

    def parcourirTuple(self, personnage) :
        for element in personnage :
                element = str(element)
                print(element)

    #fonction str 

    def __str__(self) : 
        self.parcourirTuple(personnage)
        return str(self.nom) + " " + str(self.prenom) + " " + str(self.personnage)

        

def nbPersonnages(personnage) :
    compteur = 0
    for nb_personnages in personnage :
        compteur += 1
    return compteur, nb_personnages 


personnage = (P5.__str__(), P6.__str__())
personnage1 = (P5, P6)
A1 = Acteur("Christensen", "Hayden", personnage1)
A2 = Acteur("Neeson", "Liam", P1)
A3 = Acteur("Christensen", "Hayden", (personnage))
print(A1.__str__())
print(A2.__str__())
print(A3.__str__())
# print(A3.__str__())


