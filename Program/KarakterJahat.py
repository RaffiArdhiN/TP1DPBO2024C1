from Karakter import Karakter

class KarakterJahat(Karakter):
    def __init__(self, nama, gender, hp, atk):
        super().__init__(nama, gender)
        self.hp = hp
        self.atk = atk
        
    def getHp(self):
        return self.hp
    
    def setHp(self, hp):
        self.hp = hp
        
    def getAtk(self):
        return self.atk
    
    def setAtk(self, atk):
        self.atk = atk
        
    def attack(self):
        print(f"{self.nama} ({self.gender}) menyerang")
        
    def talk(self):
        print("Bagaimana kabarmu?")