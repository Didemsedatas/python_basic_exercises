#kullanıcının girdiği içeceğe göre kokteyl önerileri

import streamlit as st
import json
from urllib.request import urlopen

st.header("COCTAILS")

search = st.text_input("Drink: ")
link = urlopen("https://www.thecocktaildb.com/api/json/v1/1/search.php?s="+search).read()
json_link = json.loads(link)

coctails_datas = json_link["drinks"]

for coctail in coctails_datas:
    st.write(coctail['strDrink'])
    st.image(coctail['strDrinkThumb'])
    st.write(coctail['strInstructions'])
