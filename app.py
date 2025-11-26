# Write your code here
import streamlit as  st
import pandas  as pd
from utils import predict_species
import joblib
 
model  =  joblib.load("notebook/iris_model.joblib")
 
#  design page  
 
st.set_page_config(page_title= 'Iris  end  to end  deployment' ,  layout='wide')
 
#  give  title
st.title('Iris  Deployment  for  end  user')
 
#  give  name
 
st.subheader('By sakshi landge')

#take input from user
sep_len=st.number_input("sepal_length",min_value=0.00,step=0.01)
sep_wid=st.number_input("sepal_width",min_value=0.00,step=0.01)
petal_len=st.number_input("petal_length",min_value=0.00,step=0.01)
petal_wid=st.number_input("sepal_width",min_value=0.00,step=0.01)

pred=predict_species(model,sep_len,sep_wid,petal_len,petal_wid)

#add button
predict=st.button("prediction",type="primary")
if  predict:
    pred ,  prob   =  predict_species(model  ,  sep_len  ,  sep_wid  ,  petal_len , petal_wid)
 
    st.subheader(pred)
    probs  =  st.dataframe(prob)
    st.subheader(probs)
                   

