import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# 1. Welcome message and page configuration
st.markdown(
    """
    <h2 style='text-align: center; color: #9a0840;'>
        🚗💥Welcome to the Car Dashboard 💥🚗
    </h2>
    <p style='text-align: center; color: #555; font-size: 18px;'>
        Explore US car crash statistics, trends, and insights interactively!
    </p>
    """,
    unsafe_allow_html=True
)
st.write("This dashboard provides insights into car data, including accidents, speeding, and alcohol involvement.")


#2. Add a thematic image
st.image(
    'https://i.cbc.ca/1.5631055.1703014113!/fileImage/httpImage/image.jpg_gen/derivatives/original_1180/rawlins-cross-crash.jpg?im=width=1180&quality=70&size=1180x663',
)
st.image('https://aarp.widen.net/content/qiur2bsr5d/jpeg/GettyImages-451333971-web.jpg?crop=true&anchor=18,61&q=80&color=ffffffff&u=k2e9ec&w=2021&h=1161')

#3. Load the dataset
df = sns.load_dataset("car_crashes") 

#4. Key metrics section
col1, col2, col3 = st.columns(3)
col1.metric("Total Accidents", df['total'].sum())
col2.metric("Average Speeding", df['speeding'].mean())
col3.metric("Average Alcohol Involvement", df['alcohol'].mean())





        