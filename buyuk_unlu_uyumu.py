#kullanıcıdan alınan kelimenin büyük ünlü uyumuna uygunluğunun değerlendirilmesi

kelime = input("kelime giriniz: ")
kelime = kelime.lower()

kalın_harfler = ["a", "ı", "o", "u"]
ince_harfler = ["e", "i", "ö" , "ü"]

kalın_say = 0
ince_say = 0


for i in kelime:
  if i in kalın_harfler:
    kalın_say = kalın_say+1
  if i in ince_harfler:
    ince_say = ince_say+1


if kalın_say+ince_say == 1:
  print("Büyük ünlü uyumu aranmaz.")

elif kalın_say*ince_say == 0:
  print("Büyük ünlü uyumuna uyar.")

else:
  print("Büyük ünlü uyumuna uymaz.")