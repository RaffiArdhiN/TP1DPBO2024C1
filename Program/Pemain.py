from KarakterPlayer import KarakterPlayer

class Pemain :
    def __init__(self, nama, karakter=None):
        self.nama = nama
        self.karakter = karakter
        
    def getNama(self):
        return self.nama
    
    def setNama(self, nama):
        self.nama = nama
        
    def getKarakterPlayer(self):
        return self.karakter
    
    def setKarakterPlayer(self, karakter):
        self.karakter = karakter