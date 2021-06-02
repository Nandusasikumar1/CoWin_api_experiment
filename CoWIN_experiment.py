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
    date=st.text_input('Enter date(mm-dd-yyyy)',value='01-06-2021',key=2)
    districts=st.selectbox('Select District',list(file['districts']))
    dist_id=list(file[file['districts']==districts]['district_id'])[0]
    response=requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?',params={'district_id':str(dist_id),'date':date})
    return response
def data_frame():
    response=cowin_data()
    c=[]
    for i in response.json():
        for k in response.json()[i]:
            c.append(k)
    return c

def show():
    st.set_page_config(page_title="Nandu's CoWin api experiment")
    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.write(st.dataframe(data_frame()))
show()
