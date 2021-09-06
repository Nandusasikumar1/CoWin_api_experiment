#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np 
import requests
import streamlit as st
file=pd.read_csv('cowinkerala.csv')
st.set_page_config(page_title="Nandu's cowin slot finder")
date=st.date_input('Enter Date (day-month-year)')
districts=st.selectbox('Select District',list(file['districts']))
dist_id=list(file[file['districts']==districts]['district_id'])[0]
response=requests.get(f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={dist_id}&date={date}')
l={}
for i in response.json()['sessions']:
    l[i['block_name']]=[i['address'],i['pincode'],i['available_capacity_dose1'],i['available_capacity_dose2']]
display_data=pd.DataFrame(l,index=['address','pin','available_capacity_dose1','available_capacity_dose2']).T
st.dataframe(display_data)

