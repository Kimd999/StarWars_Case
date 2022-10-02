from PersoSW import Personnage

class Gentil(Personnage) : 

    def __init__(self, force) :
        self.force = force

    def setCoteForce(self, force)  :
        self.force = force

    def setCoteForce(self) : 
        return self.force

    def __str__(self) : 
        return bool(self.force)