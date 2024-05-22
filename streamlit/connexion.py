import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import multipage_option_menu

with open('config.yml') as file:
    config = yaml.load(file, Loader=SafeLoader)

#print(config['credentials'])
#>>>
#{'usernames': {'jsmith': {'email': 'jsmith@gmail.com', 'failed_login_attempts': 0, 'logged_in': False, 'name': 'John Smith', 'password': 'abc'}, 'rbriggs': {'email': 'rbriggs@gmail.com', 'failed_login_attempts': 0, 'logged_in': False, 'name': 'Rebecca Briggs', 'password': 'def'}}}
#{'usernames': {'jsmith': {'email': 'jsmith@gmail.com', 'failed_login_attempts': 0, 'logged_in': False, 'name': 'John Smith', 'password': 'abc'}, 'rbriggs': {'email': 'rbriggs@gmail.com', 'failed_login_attempts': 0, 'logged_in': False, 'name': 'Rebecca Briggs', 'password': 'def'}}}

authenticator = stauth.Authenticate(
    {'usernames': {'jsmith': {'email': 'jsmith@gmail.com', 'failed_login_attempts': 0, 'logged_in': False, 'name': 'John Smith', 'password': 'abc'}, 'rbriggs': {'email': 'rbriggs@gmail.com', 'failed_login_attempts': 0, 'logged_in': False, 'name': 'Rebecca Briggs', 'password': 'def'}}},#config['credentials'],
    "toto", #config['cookie']['name'],
    "toto", #config['cookie']['key'],
   30, #config['cookie']['expiry_days'],
    "test", #1config['pre-authorized']
)

authenticator.login()

if st.session_state["authentication_status"]:
    authenticator.logout("Déconnexion")
    #st.title('Some content')
    multipage_option_menu.lancement()
    st.write(f'Welcome *{st.session_state["name"]}*')

elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')
