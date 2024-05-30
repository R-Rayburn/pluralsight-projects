import streamlit as st

st.title("Hello Streamlit")
st.header("Calculate % Growth")
initial = st.number_input("Initial investment in USD")
yr = st.number_input("Growth Period in years")
growth = st.number_input("Growth Rate in %")
terminal_val = 0
current_val = inital
for year in range(int(yr)):
    current_val += grwoth * current_val
    terminal_val = current_val

# perform cashflow projections for the next 5 years
st.write(f'Terminal value of {initial} after {yr} years at a growth rate of {growth} is {terminal_value}')
