import streamlit as st
import pandas as pd
st.title("Programming World")
st.markdown("_Italic word_")
lan=st.selectbox("select the language:",["c++","python","java","html"])
st.write(f"Your choose {lan}
st.markdown("basic HELLO WORLD in programme language")
st.code("for python:basic
if st.button("submit"):
  st.success("your had successfully choosen the language.SUBMISSION DONE!")
add_lan=st.input("enter your fav language:")
if add_lan:
  st.success(f"your {add_lan} is added succesfully")
st.text("THANK YOU")

data = {"Name": ["Amit", "Priya", "Rahul"], "Age": [21, 25, 30]}
df = pd.DataFrame(data)

st.write("Interactive DataFrame:")
st.dataframe(df)
