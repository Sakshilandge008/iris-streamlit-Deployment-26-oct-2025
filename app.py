# Write your code here
import streamlit as  st
import pandas  as pd
from utils import predict_species
import joblib
 
model  =  joblib.load("/workspaces/Iris-Streamlit-Deployment-26-oct-2025/notebook/iris_model.joblib")
 
#  design page  
 
st.set_page_config(page_title= 'Iris  end  to end  deployment' ,  layout='wide')
 
#  give  title
st.title('Iris  Deployment  for  end  user')
 
#  give  name
 
st.subheader('By sakshi landge')
                   

