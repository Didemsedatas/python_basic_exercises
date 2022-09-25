# girilen metni ilgiliyi numaraya wpden mesaj olarak iletme.

import streamlit as st
import qrcode


def qryap(metin):
    wp = "https://wa.me/+905*********?text="+metin
    a = qrcode.make(wp)
    a.save("dosya.png")
    st.image("dosya.png") #qr kodu ekranda gösterir.




x = st.text_input("Metin Giriniz")
qryap(x)