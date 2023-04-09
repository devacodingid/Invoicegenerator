from deta import Deta
import streamlit as st

deta = Deta(st.secrets["deta_key"])
db = deta.Base("users_db")


def insert_user(username, name, password, email):
    """Returns the user on a successful user creation, otherwise raises and error"""
    return db.put({"key": username, "name": name, "password": password, "email": email })


def fetch_all_users():
    """Returns a dict of all users"""
    res = db.fetch()
    return res.items


def get_user(username):
    """If not found, the function will return None"""
    return db.get(username)


def update_user(username, updates):
    """If the item is updated, returns None. Otherwise, an exception is raised"""
    return db.update(updates, username)


def delete_user(username):
    """Always returns None, even if the key does not exist"""
    return db.delete(username)

def mycredentials():
    a = db.fetch()
    mylist = a.items
    startdict = "{'cookie': {'expiry_days': 30, 'key': 'some_signature_key', 'name': 'some_cookie_name'}, 'credentials': {'usernames': {"
    enddict = "}},'preauthorized': {'emails': ['devacodingid@gmail.com']}}"
    new1 = ''

    for x in mylist:
        new = "'"+x.get('key') + "': {'email': '" + x.get('email') +"', 'name': '" + x.get('name') +"', 'password': '"+ x.get('password')+"'},"
        new1 += new    

    new2 = new1.rstrip(new1[-1])
    finaldict = startdict + new2 + enddict
    return finaldict
