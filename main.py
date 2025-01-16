import pickle
import streamlit as st
from os import path
import numpy as np


st.title("Flower Classification App")

file_name = "lr_model.pkl"
with open(path.join("model",file_name) , 'rb') as f:
    lr_model = pickle.load(f)

sl = st.number_input("Insert a sepal length")
sw = st.number_input("Insert a sepal width")
pl = st.number_input("Insert a patal length")
pw = st.number_input("Insert a patal width")

if st.button("Predict"):
    pred = lr_model.predict(np.array([[sl, sw, pl, pw]]))
    st.write("The flower is:", pred[0])

