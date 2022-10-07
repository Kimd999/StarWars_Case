#class pour créer les acteurs
from xml.dom import NO_MODIFICATION_ALLOWED_ERR
from PersoSW import *

class Acteur : 

    def __init__(self, nom, prenom, personnage) :
        self.setNom(nom)
        self.setPrenom(prenom)
        self.setPersonnage(personnage)        

    #setters 

    def setNom(self, nom) : 
        self.nom = nom 
    
    def setPrenom(self, prenom) : 
        self.prenom = prenom 
    
    def setPersonnage(self, personnage) :

        self.personnage = personnage

    #getters 
    
    def getNom(self) :
        return self.nom

    def getPrenom(self) : 
        return self.prenom
    
    def getPersonnage(self) :

        return self.personnage


#méthode pour ajouter un personnage au tuple vide
    
    def parcourirTuple(self):

        personnage = list(self.getPersonnage())
        stri = ""
        i = 0
        while i < len(personnage):

            stri += " interprète " + personnage[i].__str__() + "  et " 
            i += 1
        stri = stri[:-4]

          
        return stri

    #fonction str 

    def __str__(self) : 
   
        return str(self.nom) + " " + str(self.prenom) + " " + self.parcourirTuple()

        

    def nbPersonnages(self) :
        return len(list(self.getPersonnage()))






A1 = Acteur("Christensen", "Hayden", (P5, P6))
A2 = Acteur('McDiarmid', "Ian", (P2, P2b))
print(A2.nbPersonnages())

print(A1)
print(A2)



