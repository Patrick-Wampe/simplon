import streamlit as st

def lancement():
    prenom = st.text_input("Indique ton prénom")
    photoURL = st.text_input("Indique l'url de ta photo")
    validation = st.button("Valider")

    if validation:
        st.session_state["prenom"] = prenom
        st.session_state["photoURL"] = photoURL

