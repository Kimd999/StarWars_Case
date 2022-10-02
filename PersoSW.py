class Personnage : 

    def __init__ (self, nom_perso, prenom_perso) :
        self.setNomPerso(nom_perso)
        self.setPrenomPerso(prenom_perso)

    #getters 

    def setNomPerso(self, nom_perso) : 
        self.nom_perso = nom_perso
    
    def setPrenomPerso(self, prenom_perso) : 
        self.prenom_perso = prenom_perso
    
    #setters 

    def getNomPerso(self) :
        return self.nom_perso

    def getPrenomPerso(self) : 
        return self.prenom_perso
    
    #fonction str 
 
    def __str__(self) : 
        return str(self.nom_perso) + " " + str(self.prenom_perso)
    

P1 = Personnage('Jinn', 'Qui-Gon')
P2 = Personnage("Palpatine", 'Sheev')
P3 = Personnage("Tano", "Ashoka")
P4 = Personnage("Amidala", "Padmé")
P5 = Personnage("Vader", "Darth")
P6 = Personnage('Skywalker', "Anakin")



#collection_Personnage = [P1, P2, P3, P4]