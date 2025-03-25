class lkan:
    def __init__(self,x,y,z,a):
        self.name = x
        self.surname = y
        self.age = z
        self.rank = a
    def info(self):
        print(f"ADINIZ:{self.name}  SOYAD:{self.surname}  YAŞ:{self.age}  RUTBE:{self.rank}")
print("ŞİRKETİMİZE HOŞGELDİNİZ")
print("KAYIT OLMAK İÇİN 1'e BASINIZ.")
print("ZİYARET ETMEYE GELDİYSENİZ 2'ye BASINIZ")
giriş1 = input("Nasıl bir işlem yapmak istiyorsunuz:")
giriş = int(giriş1)
if giriş == 1:
       x = input("ADINIZI GİRİNİZ:")
       y = input("SOYADINIZI GİRİNİZ:")
       z = input("YAŞINIZI GİRİNİZ:")
       a = ("üye")
       print("KAYIT BAŞARILI")
       giriş = lkan(x,y,z,a)
       print("ŞİRKET KARTINIZ")
       print(giriş.info())
elif giriş == 2:
       print("HOŞGELDİNİZ GEZEBİLİRSİNİZ")
print("bitti")

