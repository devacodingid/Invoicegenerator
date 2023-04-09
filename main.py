import streamlit as st
import streamlit_authenticator as stauth
import database as db

#st.set_page_config(layout='wide')
st.title ('Hey, this is a new app')
hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)

myconfig = db.mycredentials()
config = ast.literal_eval(myconfig)

# Creating the authenticator object
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'], 
    config['cookie']['key'], 
    config['cookie']['expiry_days'],
    config['preauthorized']
    )

# creating a login widget
name, authentication_status, username = authenticator.login('Login', 'main')
if authentication_status:
    st.sidebar.title(f'Welcome *{name}*')
    st.sidebar.text('You are a premium member')
    authenticator.logout('Logout', 'sidebar')

elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')