class Personnage : 

    def __init__ (self, prenom_perso, nom_perso) :
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
        return str(self.prenom_perso) + " " + str(self.nom_perso)
    

    #Création de personnages

P1 = Personnage('Qui-Gon', 'Jinn')
P2 = Personnage("Sheev", 'Palpatine')
P2b = Personnage("Darth", "Sidious")
P3 = Personnage("Ashoka", "Tano")
P4 = Personnage("Padmé", "Amidala")
P5 = Personnage("Darth", "Vader")
P6 = Personnage('Anakin', "Skywalker")




