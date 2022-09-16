#yıllık kazanca göre gelir vergisi hesaplama
#https://www.rasyoneldanismanlik.com/2022-yili-gelir-vergisi-dilimleri-aciklandi

kazanc = float(input("Yıllık kazancınızı giriniz: "))

v32=32000*0.15
v70=(70000-32000)*0.20
v250=(170000-70000)*0.27
v880=(880000-170000)*0.35


if kazanc < 32000:
  vergi = kazanc*0.15
elif kazanc < 70000:
  vergi = ((kazanc - 32000)*0.20)+v32
elif kazanc < 250000:
  vergi = ((kazanc - 70000)*0.27)+v70+v32
elif kazanc < 880000:
  vergi = ((kazanc - 250000)*0.35)+v250+v70+v32
else:
  vergi = ((kazanc - 880000)*0.40)+v880+v250+v70+v32

print("Yıllık ödemeniz gereken vergi tutarı: ", vergi)