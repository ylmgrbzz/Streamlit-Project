import streamlit as st
from functions import *
st.header("Modeller")
with st.expander("Model Ekle"):
    with st.form("modelekle",clear_on_submit=True):
        marka=st.selectbox("Marka Seçiniz",["Audi","BMW","Mercedes","Opel","Volkswagen"])
        model=st.text_input("Marka Giriniz")
        yil=st.number_input("Yıl Giriniz",step=1,value=2022)
        submitted=st.form_submit_button("Model Ekle")
        if submitted:
            modelekle(marka,model,yil)
tabloyap("modeller",["Marka","Model","Yıl"])


