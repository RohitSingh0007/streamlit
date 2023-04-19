import streamlit as st

def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

st.title("Find the Largest Among 3 Numbers")

num1 = st.number_input("Enter the first number:", value=0)
num2 = st.number_input("Enter the second number:", value=0)
num3 = st.number_input("Enter the third number:", value=0)

if st.button("Find the Largest"):
    largest_num = find_largest(num1, num2, num3)
    st.write("The largest number is:", largest_num)
