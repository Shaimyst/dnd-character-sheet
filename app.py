import streamlit as st

# Title of the app
st.title("Hello World!")

# Display text
st.write("Welcome to your first Streamlit app!")

# Interactive input
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}! 👋")
