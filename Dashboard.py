import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.header("The Best Company")

context= """This app showcases the cream of the crop in the business world.
Powered by data analysis and user feedback, 
it highlights top-performing companies across industries.
Explore company profiles, key metrics, and industry trends with ease. 
Join us in celebrating excellence and innovation in business.
"""

st.write(context)

st.subheader("Our Team")


col1, col2, col3 = st.columns(3)

df = pd.read_csv("data (1).csv")

with col1:
    for index, row in df[:4].iterrows():
        st.header(f"{row['first name'].title()} {row['last name']}")
        st.subheader(row["role"])
        st.image("images (1)/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.header(f"{row['first name'].title()} {row['last name']}")
        st.subheader(row["role"])
        st.image("images (1)/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.header(f"{row['first name'].title()} {row['last name']}")
        st.subheader(row["role"])
        st.image("images (1)/" + row["image"])