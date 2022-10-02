from PersoSW import Personnage

class Mechant(Personnage) :

    def __init__(self, cote_obscur) :
        self.cote_obscur = cote_obscur

    def setCoteObscur(self, cote_obscur) : 
        self.cote_obscur = cote_obscur

    def getCoteObscur(self) :
        return self.cote_obscur

    def __str__(self) : 
        return bool(self.cote_obscur)