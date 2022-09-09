import streamlit as st
st.set_page_config(layout="wide")
st.header("Ana Sayfa")
from functions import *
st.subheader("Günün Randevuları")
gununrandevu()
