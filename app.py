import streamlit as st


st.markdown("<h1 style='text-align: center; color: red;'>CalcGPA</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; '>Semester GPA Calculator of B.Tech(IT)</h3>", unsafe_allow_html=True)

name = st.text_input("Enter your name:")
sem = st.number_input("Enter your semester:", 1, 6)

#st.write(sem)

