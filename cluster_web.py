import streamlit as st 
import pandas as pd 
import numpy as np 
import pickle as pk
import os

data = pk.load(open('cluster.sav', 'rb'))
scaler = pk.load(open('scaler.sav', 'rb'))

st.title('توقع الشخص ينتمي لاي فئة من الفئات الخمسة')

gander_map = {'female':0,'male':1}


Genre = st.selectbox('gender',options=list(gander_map.keys()))
Age = st.number_input('Age')
Annual_Income = st.number_input('Annual Income (k$)')
Spending_Score = st.number_input('Spending Score (1-100)')

con = st.button('تحليل')

if con:
    input_data = [Genre,Age,Annual_Income,Spending_Score]
    cols = ['Genre','Age','Annual Income (k$)','Spending Score (1-100)']
    df=pd.DataFrame([input_data],columns=cols)
    df['Genre'] = df['Genre'].map(gander_map)


    cols_scale = ['Age','Annual Income (k$)','Spending Score (1-100)']
    df[cols_scale] = scaler.transform(df[cols_scale])

    pred = data.predict(df.values)


    if pred[0] == 0:
        st.write('انه من الفئة الاولي')

    if pred[0] == 1:
        st.write('انه من الفئة الثانية')

    if pred[0] == 2:
        st.write('انه من الفئة الثالثة')

    if pred[0] == 3:
        st.write('انه من الفئة الرابعة')

    if pred[0] == 4:
        st.write('انه من الفئة الخامسة')