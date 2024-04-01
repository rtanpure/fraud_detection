# -*- coding: utf-8 -*-
"""
Created on Sat march 20 15:09:52 2022

@author: rtanp
"""
import streamlit as st
import numpy as np
import pandas as pd
import pickle


pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)


def welcome():
    return "Welcome all"

def fraud_pred(type_,amount,oldbalanceOrig,newbalanceOrig):
    prediction=classifier.predict([[type_,amount,oldbalanceOrig,newbalanceOrig]])
    print(prediction)
    return prediction
    
def main():
    st.title("Fraud Detection")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Fraud Detection ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    type_ = st.text_input("Type","1 to 5")
    amount = st.text_input("Amount","number")
    oldbalanceOrig = st.text_input("Old Balance","number")
    newbalanceOrig = st.text_input("New balance","number")
    result=""
    if st.button("Predict"):
        result=fraud_pred(type_,amount,oldbalanceOrig,newbalanceOrig)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Made By Rishabh Tanpure")
        st.text("app built with Streamlit")
    
    
    
if __name__=='__main__':
    main()
