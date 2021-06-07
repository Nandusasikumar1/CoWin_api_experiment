import pandas as pd
import numpy as np 
import requests
import streamlit as st
class cowin():
    def read(self):
        file1=pd.DataFrame({'district_id':[295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308],
                          'districts':['Kasaragod','Thiruvananthapuram','Kannur','Kollam','Wayanad','Pathanamthitta','Alappuzha','Malappuram','Thrissur','Kottayam','Kozhikode','Idukki','Ernakulam','Palakkad']
                          })
        return file1
    def cowin_data(self):
        file=self.read()
        date=st.text_input('Enter date(mm-dd-yyyy)',value='01-06-2021',key=2)
        districts=st.selectbox('Select District',list(file['districts']))
        dist_id=list(file[file['districts']==districts]['district_id'])[0]
        response=requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?',params={'district_id':str(dist_id),'date':date})
        c=[]
        try:
            for i in response.json():
                for k in response.json()[i]:
                    c.append(k)
            keyss=[i.keys() for i in c]
            keys1=list(np.unique(keyss)[0])
            index=[keys1.index(i) for i in ['name','pincode','fee_type','min_age_limit','vaccine','available_capacity_dose1','available_capacity_dose2']]
            data={}
            for f in index:
                data[keys1[f]]=[]
                for p in c:
                    data[keys1[f]].append(list(p.values())[f])
            return data
        except:
            st.write('No center available')

    def show(self):
        st.set_page_config(page_title="Nandu's CoWin api experiment")
        hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)
        df=pd.DataFrame(self.cowin_data())
        df.rename(columns={'available_capacity_dose1':'dose1','available_capacity_dose2':'dose2'},inplace=True)
        st.write(df)
if __name__=='__main__':
    cowin().show()
    
