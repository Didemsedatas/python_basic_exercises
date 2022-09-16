##isim, soyisim, domain ile ünlü harfleri olmayan mail oluşturma (isim ve soyismin baş harfleri sesli olsa da kalmalıdır.)

isim=input("isim giriniz: ")
soyisim=input("soyisim giriniz: ")
domain=input("domain giriniz: ")

isim = isim.lower()
isim = isim.replace("ç","c")
isim = isim.replace("ı","i")
isim = isim.replace("ü","u")
isim = isim.replace("ö","o")
isim = isim.replace("ğ","g")
isim = isim.replace("ş","s")

soyisim = soyisim.lower()
soyisim = soyisim.replace("ç","c")
soyisim = soyisim.replace("ı","")
soyisim = soyisim.replace("ü","")
soyisim = soyisim.replace("ö","")
soyisim = soyisim.replace("ğ","g")
soyisim = soyisim.replace("ş","s")

domain = domain.lower()
domain = "@"+domain

isim_ilk_harf = isim[0]
isim_kalan = isim[1:]

soyisim_ilk_harf = soyisim[0]
soyisim_kalan = soyisim[1:]

isim_kalan = isim_kalan.replace("a","")
isim_kalan = isim_kalan.replace("e","")
isim_kalan = isim_kalan.replace("i","")
isim_kalan = isim_kalan.replace("o","")
isim_kalan = isim_kalan.replace("u","")

soyisim_kalan = soyisim_kalan.replace("a","")
soyisim_kalan = soyisim_kalan.replace("e","")
soyisim_kalan = soyisim_kalan.replace("i","")
soyisim_kalan = soyisim_kalan.replace("o","")
soyisim_kalan = soyisim_kalan.replace("u","")


mail = isim_ilk_harf+isim_kalan+soyisim_ilk_harf+soyisim_kalan+domain

print("mail adresiniz: ",mail)
 
