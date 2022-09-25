# instagram profil fotoğrafını getirme

import streamlit as st
import instaloader
import os
os.listdir()

resim = st.text_input("kullanıcı adı giriniz")
if len(resim)>0:
    instagram = instaloader.Instaloader()
    instagram.download_profile(resim, profile_pic_only=True)
    cikti=os.listdir(resim)
    link = resim+"/"+cikti[0]
    st.image(link)

else:
    st.write("örnek: robertdowneyjr")