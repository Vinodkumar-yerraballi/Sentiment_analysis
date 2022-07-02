import streamlit as st
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from PIL import Image


data=pd.read_csv('Twitter_Data.csv')
data.dropna(inplace=True)

X=np.array(data['clean_text'])
y=np.array(data['category'])
vector=TfidfVectorizer()
X=vector.fit_transform(X)
model=LogisticRegression()
model.fit(X,y)

image3=Image.open('download.jpeg')

def main():
  st.title("Sentimental analysis")
  st.markdown(
        """
        <style>
            .reportview-container {background-color:Pink;}
        </style>
        """,
        unsafe_allow_html=True)
  st.markdown("""
    <div style="background-color:Yellow;padding:10px">
        <h2 style="color:Black;text-align:center;">Sentimental Analysis App </h2>
    </div>
    """, unsafe_allow_html=True)
  st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
  user=st.text_area("Enter text hear:","Type hear")
  st.button("Predict")
  if len(user)<1:
      st.write(" ")
  else:
    user=vector.transform([user]).toarray()
    result=model.predict(user)
    if result ==[1.]:
      image=Image.open('images.jpeg')
      st.image(image,caption="Positive Sentiment")
      st.balloons()
    elif result == [-1.]:
        image=Image.open('images (1).jpeg')
        st.image(image,caption="Negative Sentiment")
    else:
	      st.image(image3,caption="Netural sentimetn")
        
        
      




if __name__=='__main__':
    main()


  
