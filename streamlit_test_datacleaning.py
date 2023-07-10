import streamlit as st
import pandas as pd
import numpy as np
import re

TEST_DATA = pd.read_excel('smartsheet_testSheet.xlsx')

TRUCKS = list(TEST_DATA['Primary'])
TRUCKS_AND_ROW_NUMS = [(row_num, TEST_DATA.loc[row_num, 'Primary']) for row_num in TEST_DATA.index]
TRUCKS_AND_ROW_NUMS_DICT = {row_num: TEST_DATA.loc[row_num, 'Primary'] for row_num in TEST_DATA.index}
# print(TRUCKS_AND_ROW_NUMS_DICT)

new_dict = {}
for ind, truck in TRUCKS_AND_ROW_NUMS_DICT.items():
    truck_num = re.findall(r"(?:E9|ZZ)(\d{4})", str(truck))

    if truck_num:
        new_dict[ind] = (truck_num[0], truck)

def get_trucks_dict():
    return TRUCKS_AND_ROW_NUMS_DICT