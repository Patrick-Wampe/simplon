import streamlit as st
import seaborn as sns
import sklearn
import tinydb
from streamlit_option_menu import option_menu
import photos
import videos
import prenom

#with st.sidebar:
#    choix = option_menu(
#        menu_icon="bi bi-box-seam-fill",
#        menu_title="Menu",
#        options=["Accueil", "Photos", "Vidéos", "Qui es-tu ?"],
#        default_index=0,
#        orientation="vertical",
#    )

#with st.sidebar:
#    st.title("Hello je suis une sidebar !")

choix = option_menu(
        menu_icon="bi bi-box-seam-fill",
        menu_title="Menu",
        options=["Accueil", "Photos", "Vidéos", "Qui es-tu ?"],
        default_index=0,
        orientation="horizontal",
        styles={
            "icon" : {"color" : "red"},
        }
    )

if "prenom" not in st.session_state:
    st.session_state["prenom"] = ""
if "photoURL" not in st.session_state:
    st.session_state["photoURL"] = ""

if choix == "Accueil":
    st.title(f"Hello {st.session_state['prenom']} !")
elif choix == "Photos":
    #st.title("Mes photos")
    photos.lancement()
elif choix == "Vidéos":
    #st.title("Mes vidéos")
    videos.lancement()
elif choix == "Qui es-tu ?":
    prenom.lancement()
