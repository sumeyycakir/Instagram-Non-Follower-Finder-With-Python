import instaloader
import kullaniciBilgileri as kb

instagram = instaloader.Instaloader()
instagram.login(kb.kAdi,kb.sifre)

profil = instaloader.Profile.from_username(instagram.context, "") # Instagram kullanıcı adını yaz

takipciler = profil.get_followers()
takipcilerListesi = list()
takipEdilenlerListesi = list()

for i in takipciler:
    takipcilerListesi.append(i.username)

takipEdilenler = profil.get_followees()

for i in takipEdilenler:
    takipEdilenlerListesi.append(i.username)

for i in takipEdilenlerListesi:
    if i not in takipcilerListesi:
        print(i + " Seni takip etmiyor.")
