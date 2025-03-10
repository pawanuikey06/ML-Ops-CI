import streamlit as st


st.title("Power Calculator")
st.write("Enter a number to Calculate its square,cube,and fifth Power")

# Get User Input
n=st.number_input("Enter an Integer",value=1,step=1)


# Calculate Results
square=n**2
cube=n**3
fifth_power=n**5

st.write(f"The Square of {n} is : {square}")
st.write(f"The Cube of {n} is : {cube}")
st.write(f"The fifth power of {n} is :{fifth_power}")
