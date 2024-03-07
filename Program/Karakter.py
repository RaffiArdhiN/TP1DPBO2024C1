class Karakter:
    def __init__(self, nama, gender):
        self.nama = nama
        self.gender = gender
        
    def getNama(self):
        return self.nama
    
    def setNama(self, nama):
        self.nama = nama
        
    def getGender(self):
        return self.gender
    
    def setGender(self, gender):
        self.gender = gender