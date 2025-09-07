import streamlit as st
st.title("programming world")
st.text("WELCOME TO PROFRAMMING EARTH")
lan=st.selectbox("select the language:",["c++","python","java","html"])
st.write(f"Your choose {lan}.Excellent choice")
if st.button("submit"):
  st.success("your had successfully choosen the language.SUBMISSION DONE!")
st.success("your lan has been breded")
st.text("THANK YOU")
