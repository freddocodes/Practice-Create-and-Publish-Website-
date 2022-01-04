import streamlit as st
import pandas


data= {
  'Series_1':[1, 3, 4, 5, 7],
  'Series_2':[10, 30, 40, 100, 250]
}

df= pandas.DataFrame(data)

st.title('Our First Streamlit App')
st.subheader('Introduction to Streamlit in Class')
st.write('this is my first Web App.')
st.write(df)