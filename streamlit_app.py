import streamlit as st

st.title('Streamlit Layouts Demo')

col1, col2 = st.columns(2)
with col1:
  st.header("Column 1")
  st.write("Hello")

with col2:
  st.header("Column 2")
  st.write("World")

with st.expander("See explanation"):
  st.write("Here you could put in some really, really explanatory stuff.")
