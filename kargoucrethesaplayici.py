class paket:
    def __init__(self,paketID,paketAgirlik,gidecegiToplamKm,gondericiAdi,aliciAdi):
        self.paketID = paketID
        self.paketAgirlik = paketAgirlik
        self.gidecegiToplamKm = gidecegiToplamKm
        self.gondericiAdi = gondericiAdi
        self.aliciAdi = aliciAdi

        
    def ucretHesaplama(self,gönderiÜcreti):
        self.gönderiÜcreti=gönderiÜcreti
       
        if self.gönderiÜcreti==0.2:
             ucret1 = self.gidecegiToplamKm *0.2
             print("Standart Ücret:",ucret1)
        if self.gönderiÜcreti==0.5:  
             ucret2 = self.gidecegiToplamKm *0.5
             print("Express Ücret:",ucret2)


class standartPaket(paket):
    def __init__(self,standartGonderimUcreti):
        self.standartGonderimUcreti = standartGonderimUcreti
        

    def bilgiler(self):
        print("Paket ID numarası:", self.paketID)
        print("Paket ağırlığı:", self.paketAgirlik)
        print("Gideceği km:", self.gidecegiToplamKm)
        print("Gönderici adı:", self.gondericiAdi)
        print("Alıcı adı:", self.aliciAdi)
        

class expressPaket(paket):
    def __init__(self,expressGonderimUcreti):
        self.expressGonderimUcreti = expressGonderimUcreti
        
   
    def bilgiler(self):
        print("Gönderici adı:", self.gondericiAdi)
        print("Alıcı adı:", self.aliciAdi)
        print("Paket ID numarası:", self.paketID)
        print("Paket ağırlığı:", self.paketAgirlik)
        print("Gideceği km:", self.gidecegiToplamKm)
       



obj1 = standartPaket(0.2)
obj1.paketID = "123"
obj1.paketAgirlik = 10
obj1.gidecegiToplamKm =1500
obj1.gondericiAdi = "Mete Cakir"
obj1.aliciAdi = "Aysen Cakir"
obj1.bilgiler()
obj1.ucretHesaplama(0.2)
print("\n \n")
obj2 = expressPaket(0.5)
obj2.paketID = "456"
obj2.paketAgirlik = 20
obj2.gidecegiToplamKm = 1000
obj2.gondericiAdi = "Akif Yigit"
obj2.aliciAdi = "Miray Yilmaz"
obj2.bilgiler()
obj2.ucretHesaplama(0.5)
