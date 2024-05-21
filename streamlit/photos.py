import streamlit as st

def lancement():
    st.title(f"Les photos de vacances de {st.session_state['prenom']}")
    try:
        st.image(f"{st.session_state['photoURL']}")
    except:
        pass
