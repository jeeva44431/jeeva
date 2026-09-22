import streamlit as st

a=st.number_input("Enter a number")
b=st.number_input("Enter another number")
if-st.button("add"):
	st.success(a+b)
elif st.button("subtract"):
	st.success(a-b)
elif st.button("multiply"):
	st.success(a*b)