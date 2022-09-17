## En az 8 karakterden oluşan; büyük harf, küçük harf, sayı ve noktalama işareti içermesi gereken şifre kontrolü.

import string

sifre= input("Lütfen şifrenizi giriniz: ")

buyuk_harfler = string.ascii_uppercase
kucuk_harfler = string.ascii_lowercase
sayi = string.digits
sembol = string.punctuation

bcheck = False     # bu değişkenleri tanımlamazsak değişkenler tanımlı olmadığı için hata verir
kcheck = False
sacheck = False 
scheck = False

if len(sifre) > 8:
  for b in buyuk_harfler:
    if b in sifre:
      bcheck = True
      break
  for k in kucuk_harfler:
    if k in sifre:
      kcheck = True
      break
  for sa in sayi:
    if sa in sifre:
      sacheck = True
      break
  for s in sembol:
    if s in sifre:
      scheck = True
      break

if bcheck and kcheck and sacheck and scheck:
  print("Şifreniz başarıyla oluşturuldu.")
else: 
  print("Şifreniz en az 8 karakterden oluşmalıdır. Büyük harf, küçük harf, sayı ve noktalama işareti içermelidir.")
