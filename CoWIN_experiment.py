import pandas as pd
import numpy as np 
import requests
import streamlit as st
def cowin_data():
    file=pd.read_csv('https://raw.githubusercontent.com/Nandusasikumar1/CoWin_api_experiment/main/cowinkerala.csv')
    st.set_page_config(page_title="Nandu's CoWIN api experiment")
    
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
    pd.set_option('max_colwidth', 100)
    st.write(pd.DataFrame(l))           
if __name__ == "__main__":
    cowin_data()
