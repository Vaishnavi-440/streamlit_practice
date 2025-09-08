import streamlit as st
st.title("Programming World")
st.markdown("WELCOME TO PROFRAMMING EARTH")
lan=st.selectbox("select the language:",["c++","python","java","html"])
st.write(f"Your choose {lan}.Excellent choice")
if st.button("submit"):
  st.success("your had successfully choosen the language.SUBMISSION DONE!")
add_lan=st.input("enter your fav language:")
if add_lan:
  st.success(f"your {add_lan} is added succesfully")
st.text("THANK YOU")
