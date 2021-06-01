import pandas as pd
import numpy as np 
import requests
import streamlit as st
def read():
    file1=pd.DataFrame({'district_id':[295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308],
                      'districts':['Kasaragod','Thiruvananthapuram','Kannur','Kollam','Wayanad','Pathanamthitta','Alappuzha','Malappuram','Thrissur','Kottayam','Kozhikode','Idukki','Ernakulam','Palakkad']
                      })
    return file1
def cowin_data():
    file=read()
    st.set_page_config(page_title="Nandu's CoWin api experiment")
    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.title('Vaccination Center Finder')
    date=st.text_input('Enter date(mm-dd-yyyy)',value='01-06-2021')
    districts=st.selectbox('Select District',list(file['districts']))
    st.title('Vaccination Centers')
    dist_id=list(file[file['districts']==districts]['district_id'])[0]
    response=requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?',params={'district_id':str(dist_id),'date':date})
    l=pd.DataFrame(columns=['Address','Pin','Dose1','Dose2','Min_age_limit','Vaccine','Fee_type'])
    for i in response.json():
        for k in response.json()[i]:
            l=pd.concat([l,pd.DataFrame([[k['name'],k['pincode'],k['available_capacity_dose1'],k['available_capacity_dose2'],k['min_age_limit'],k['vaccine'],k['fee_type']]],columns=['Address','Pin','Dose1','Dose2','Min_age_limit','Vaccine','Fee_type'])],ignore_index=True)
    l.sort_values(by='Address',inplace=True)
    l.reset_index(drop='index',inplace=True)
    st.write(pd.DataFrame(l))                      
cowin_data()
