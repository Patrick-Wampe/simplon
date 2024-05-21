import streamlit as st
import seaborn as sns
import sklearn
import tinydb

st.set_page_config(
    page_title="Multipage App",
    page_icon="🤩",
)


if "prenom" not in st.session_state:
    st.session_state["prenom"] = ""

prenom = st.text_input("Indique ton prénom")
validation = st.button("Valider")

if validation:
    st.session_state["prenom"] = prenom

st.title(f"Hello {st.session_state['prenom']} !")
