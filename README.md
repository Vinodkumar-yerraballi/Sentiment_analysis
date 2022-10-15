# Sentiment_analysis

https://vinodkumar-yerraballi-sentiment-analysis-app-tp58u0.streamlitapp.com/

# Softwares used for Project

1)Python
2)Streamlit
3)Anaconda navigator
4)Visual studios

# Librarie used in data preprocessing,Modeling

           1)pandas
           2)matplotlib
           3)scikit-learn
           4)Pillow
           5)streamlit
           6)openpyxl

# About the data

The dataset is taken from the Kaggle website and predict the the sentiment is positive or negative or netrual

### In the process of data

After we receive, firstly clean the data,in the process remove the special characters and letter are covert to lower case,
After Data cleaning the next step all the data apply the NLP process the data any charactes and values covert the lowecase and remove the unknwon characters and values,Then i applied the Tdfivectorizer for the text data coverts the array,why because our systems can't analysis the text data thats why we use it.

#### Model buliding

After the data preprocessing then ready to model bulidig in the process the data divided into train and test and 25% test data and remaing the train data.

#### Model evaluation

After that we used **Logisitc Regression** algorithms because it's classification problems,and also use classification algorithms such as **Decision tree Classification and Randomforest classification ** And finally we get the model accuracy_score.

# Deployement process

Once the process is done then move to the model deployment. We use Streamlit for model deployment, We create a function for text data taken from the user and we predict the text is either spam or ham based on the data information. Once we deployed the model in the local host then we deployed the model in streamlit cloud.
# Demo of the model 


[Screencast from 10-15-2022 03:02:26 PM.webm](https://user-images.githubusercontent.com/98636972/195979526-ce0b2414-db9a-413f-942c-11350b588195.webm)



