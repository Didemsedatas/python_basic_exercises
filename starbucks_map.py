#Dünya üzerinde starbucksların haritada görüntülenmesi

import streamlit as st
import pandas as pd

df=pd.read_json("https://raw.githubusercontent.com/mmcloughlin/starbucks/master/locations.json")
sehir=st.sidebar.selectbox("Şehir Seçiniz",df["city"].unique())
df=df[df["city"]==sehir]

st.map(df)
st.table(df)