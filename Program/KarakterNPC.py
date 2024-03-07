from Karakter import Karakter

class KarakterNPC(Karakter):
    def __init__(self, nama, gender, lokasi):
        super().__init__(nama, gender)
        self.lokasi = lokasi
    
    def getLokasi(self):
        return self.lokasi
    
    def setLokasi(self, lokasi):
        self.lokasi = lokasi
        
    def beriInfoLokasi(self):
        print(f"Anda saat ini berada di {self.lokasi}")