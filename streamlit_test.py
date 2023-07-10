import streamlit as st
import pandas as pd
import numpy as np
import re
from streamlit_test_datacleaning import new_dict, TEST_DATA




st.title('Pick a truck!')
truck_select = st.text_input('Search for a truck', value='')
# truck_select = st.selectbox('Search for a truck', set(sorted(list(new_dict.values()))))

# truck_data = TEST_DATA.loc(truck_select)

def find_truck_data_row(value):
    for k, v in new_dict.items():
        if v[0] == value:
            return k
    return None

def get_truck_data(row_num):
    for k, v in new_dict.items():
        if k == row_num:
            return v[0]

if truck_select:
    st.title(f'YOU CHOSE {truck_select}')
    st.write(TEST_DATA.loc[find_truck_data_row(truck_select)])
    # st.title(f'YOU CHOSE {find_truck_data(int(truck_select)) + 2}')
    # st.write(TEST_DATA.loc[find_truck_data(int(truck_select)) + 2])

# print(new_dict)