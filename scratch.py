import streamlit as st
import pandas as pd
import numpy as np
import re

st.title('Hello this is a test')


st.header('I am a header')

st.subheader('I am a subheader')

st.write(range(10))

if st.checkbox('Show/Hide'):
    st.text('I am showing')


TEST_DATA = pd.read_excel('smartsheet_testSheet.xlsx')

st.header('this is where the data comes from')
st.write(TEST_DATA)

st.header("these are the ECU's")
ECUS = set(TEST_DATA['ECU Name'])
st.write(set(ECUS))


TRUCKS = list(TEST_DATA['Primary'])
checker = st.selectbox("Select an ECU", ECUS)
if checker:
    st.title(f'I am a representation of ECU #{checker}')
    # st.write(f'{checker}')
    # if checker:

matches = re.findall(r"E9(\d{4})", ' '.join(str(itm) for itm in TRUCKS))
unique_matches = set(matches)
sorted_matches = sorted(list(unique_matches))
truck_select = st.selectbox('Choose a truck', sorted_matches)
if truck_select:
    st.title('Pick a truck')


checker_butt = st.button(f'Show me the data for {checker}')
if checker_butt:
    st.title(f'I am the data for {checker}')
    st.header(f'{checker}')
    st.text(f'The overall status of {checker} is {TEST_DATA[TEST_DATA["ECU Name"] == "ECU Name"]}')

