from Karakter import Karakter
from Item import Item
from Role import Role

class KarakterPlayer(Karakter):
    def __init__(self, nama, gender, hp, atk, role, senjata, item=[]):
        super().__init__(nama, gender)
        self.hp = hp
        self.atk = atk
        self.role = role
        self.senjata = senjata
        self.item = item
        
    def getHp(self):
        return self.hp
        
    def setHp(self, hp):
        self.hp = hp
        
    def getAtk(self):
        return self.atk
        
    def setAtk(self, atk):
        self.atk = atk
        
    def getRoles(self):
        return self.role
        
    def setRoles(self, role):
        self.role = role
        
    def getSenjata(self):
        return self.senjata
        
    def setSenjata(self, senjata):
        self.senjata = senjata
        
    def getItem(self):
        return self.item
        
    def setItem(self, item):
        self.item = item
        
    def attack(self):
        print(f"{self.nama} ({self.gender}) menyerang dengan {self.senjata}")
        
    def quest(self):
        print(f"{self.nama} ({self.gender}) mengerjakan misi")