# Saya Raffi Ardhi Naufal NIM 2202495 mengerjakan TP 1 dalam mata kuliah DPBO untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

from Karakter import Karakter
from Pemain import Pemain
from KarakterPlayer import KarakterPlayer
from KarakterNPC import KarakterNPC
from KarakterJahat import KarakterJahat
from Item import Item
from Role import Role

def main():
    item1 = Item("Koin Emas")
    item2 = Item("Koin Silver")
    item3 = Item("Kunci")
    item4 = Item("Peta")
    item5 = Item("Ramuan")
    
    role1 = Role("Penyerang","Meningkatkan 50% atk tim")
    role2 = Role("Penyembuh","Memulihkan 50% hp tim")
    role3 = Role("Pelindung","Menjadi kebal terhadap serangan selama 10 detik")
    role4 = Role("Pembunuh","Atk meningkat 100% kepada diri sendiri")
    
    karakter1 = KarakterPlayer("Nova", 'M', 1000, 100, role1, "Panah",[item1, item2])
    karakter2 = KarakterPlayer("Jane", 'F', 1100, 70, role2, "Tongkat Sihir",[item3])
    karakter3 = KarakterPlayer("Sora", 'M', 2000, 50, role3, "Perisai",[item4])
    karakter4 = KarakterPlayer("Aloy", 'F', 500, 200, role4, "Karambit",[item5])
    
    player1 = Pemain("Fauzan", karakter1)
    player2 = Pemain("Mia", karakter2)
    player3 = Pemain("Yasin", karakter3)
    player4 = Pemain("Bintang", karakter4)
    listPlayer = [player1,player2,player3,player4]
    
    npc1 = KarakterNPC("Adrian",'M',"Bali")
    npc2 = KarakterNPC("Lyra",'F',"Jakarta")
    listNpc = [npc1,npc2]
    
    musuh1 = KarakterJahat("Thor",'M', 1000, 50)
    
    print("===============================")
    print("List Pemain :")
    print("===============================")
    for pemain in listPlayer:
        print("Pemain : ",pemain.getNama())
        print("Nama Karakter : ",pemain.getKarakterPlayer().getNama())
        print("Gender Karakter : ",pemain.getKarakterPlayer().getGender())
        print("HP : ",pemain.getKarakterPlayer().getHp())
        print("ATK : ",pemain.getKarakterPlayer().getAtk())
        print("Role : ",pemain.getKarakterPlayer().getRoles().getJenis())
        print("Skill : ",pemain.getKarakterPlayer().getRoles().getSkill())
        print("Senjata : ",pemain.getKarakterPlayer().getSenjata())
        print("Item :")
        for item in pemain.getKarakterPlayer().getItem():
            print("- ", item.getNama())
        
        print("===============================")
    print("\n")
    
    print("===============================")
    print("List NPC :")
    print("===============================")
    for npc in listNpc:
        print("Nama NPC : ",npc.getNama())
        print("Gender NPC : ",npc.getGender())
        print("Lokasi NPC : ",npc.getLokasi())
        print("===============================")
    print("\n")
    
    print("===============================")
    print("List Musuh :")
    print("===============================")
    print("Nama Musuh :",musuh1.getNama())
    print("Gender Musuh :",musuh1.getGender())
    print("HP :",musuh1.getHp())
    print("ATK :",musuh1.getAtk())
    print("===============================")
    print("\n")
    
    
    print("===============================")
    print("Method Karakter Player:")
    print("===============================")
    player1.getKarakterPlayer().attack()
    player1.getKarakterPlayer().quest()
    print("===============================")
    print("Method Karakter NPC:")
    print("===============================")
    npc1.beriInfoLokasi()
    print("===============================")
    print("Method Musuh:")
    print("===============================")
    musuh1.attack()
    musuh1.talk()
    print("===============================")
    print("\n")
    
if __name__ == "__main__":
    main()