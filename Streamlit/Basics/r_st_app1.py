import streamlit as st
import numpy as np
import pandas as pd

##Heading 
st.title("Page Title Displayed", width= "stretch")

##Displaying the 
df = pd.DataFrame(np.random.randn(5,3), columns=['A','B','C'])
st.write(df)

##Line Chart
st.line_chart(df)

##Takes text Input
nm = st.text_input("Please give your name: ")

if nm:
    st.text(f"Hi {nm}, Hope you're fine!")

##Slider
ag = st.slider("Seelect the age: ",18,100,20)
st.write(f"Your selected age is: {ag}")

##Selection Box
optn = ['CS','Java','Python','R']
optn1 = st.selectbox("Select your fav course: ",optn)
st.write(f"Your selected Language is: {optn1}")

##Multi select
optn = ['CS','Java','Python','R']
optn2 = st.multiselect("Select your fav course: ",optn)
st.write(f"Your selected Language is: {optn2}")

##Upload a File
upl= st.file_uploader("Please upload a csv or xlsx",type=['csv','xlsx'])
# st.write(upl.type)
if upl is not None:
    if upl.type == 'text/csv':
        df = pd.read_csv(upl)
        st.text("Your uploaded File:")
        st.write(df)
    elif upl.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
        df = pd.read_excel(upl)
        st.text("Your uploaded File:")
        st.write(df)
    else:
        st.text("Error: you passed non acceptable file")


