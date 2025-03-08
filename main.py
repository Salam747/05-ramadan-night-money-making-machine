import streamlit as st
import random
import time
import requests

st.title("Money Making Machine")

def generate_money():
    return random.randint(1, 1000)


def fetch_side_hustle():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustles?api_key=12345")
        if response.status_code == 200:
            hustle = response.json()  
            return hustle["side_hustle"]
        else:
            return "No side hustle available"
    except:
        return "Something went wrong"

st.subheader("Instant Cash Generator")
if st.button("Generate Money"):
    st.write("Counting your money...")
    time.sleep(1)
    amount = generate_money()
    st.success(f"You made ${amount}!")

st.subheader("Side Hustle Ideas")
if st.button("Generate Side Hustle"):
    idea = fetch_side_hustle()  
    st.success(idea)



def fetch_money_quotes():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quotes?api_key=12345")
        if response.status_code == 200:
            quotes = response.json()
            return quotes["money_quotes"]
        else: 
            return "Money is the root of all evill"
    except:
        return "Something went wrong"
st.subheader("Money makin Motivation")
if st.button("Get Inspired"):
    quote = fetch_money_quotes()
    st.info(quote)
    
    



