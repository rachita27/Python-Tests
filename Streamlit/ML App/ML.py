import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import streamlit as st

##add cache data that saves in memory 
##without need of re-running again & again

@st.cache_data
def load_iris_data():
    ##This returns the dictionary
    iris = load_iris()
    
    ##Data is key saves data
    ##iris feature names of Xs used
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    ##adding target columns that is in format 0,1,2
    df['species'] = iris.target
    ##It gives the classes name
    return df, iris.target_names


df,target_names=load_iris_data()

st.text("Display Data Imported:")
st.write(df.sample(n =6))

##Adding Sidebars
st.sidebar.title("Input Features")
sepal_length = st.sidebar.slider("Sepal length", float(df['sepal length (cm)'].min()),\
                                  float(df['sepal length (cm)'].max()))
sepal_width = st.sidebar.slider("Sepal width", float(df['sepal width (cm)'].min()),\
                                float(df['sepal width (cm)'].max()))
petal_length = st.sidebar.slider("Petal length", float(df['petal length (cm)'].min()),\
                                  float(df['petal length (cm)'].max()))
petal_width = st.sidebar.slider("Petal width", float(df['petal width (cm)'].min()),\
                                 float(df['petal width (cm)'].max()))

##Modelling part
model_rf=RandomForestClassifier()
model_rf.fit(df.iloc[:,0:4],df['species'])

data_select = [[sepal_length,sepal_width,petal_length,petal_width]]
pred = model_rf.predict(data_select)
###target names are in order
###in same order of class number: 0, 1,2
### target_names class name in same order
predicted_species = target_names[pred[0]]

st.write("Prediction")
st.write(f"The predicted species is: {predicted_species}")



