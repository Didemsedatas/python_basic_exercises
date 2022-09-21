#kullanıcı random çıkan ing kelimelerin anlamını girer, doğruluk kontrolü yapılır. 

import random

sözlük = {
    "ocean":"okyanus",
    "wave":"dalga",
    "anchor":"çapa",
    "deck":"güverte"
}


kelimeler = list(sözlük.keys())
kelime = random.choice(kelimeler)
print("Kelime: ",kelime)

cevap = input("Tahmininiz: ")

if sözlük[kelime] == cevap:
  print("Cevabınız doğru, tebrikler..")
else:
  print("Yanlış cevap, Doğru cevap: ", sözlük[kelime])
