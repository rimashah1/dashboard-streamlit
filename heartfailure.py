import streamlit as st
import pandas as pd
import numpy as np

# Load Data
DATA_URL = ('https://raw.githubusercontent.com/sauravmishra1710/Heart-Failure-Condition-And-Survival-Analysis/master/Data/heart_failure_clinical_records_dataset.csv')

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

# Load 10,000 rows of data into the dataframe.
data = load_data(10000)


# Add title
st.title('Heart Failure Data')

# Display raw data in df
st.subheader('Raw data')
st.write(data)


# Display data that we will use in df
st.subheader('Pertinent Data')
st.text('Below is the data used for the visualizations')
age_hbp = data[['age', 'platelets']]
st.write(age_hbp)


# Visualize data with area chart
st.subheader('Area Chart')
st.text('Below is the code to make an area chart')

code = '''
        age_hbp = data[['age', 'platelets']
        st.area_chart(data=age_hbp, x='age', y='platelets')
        '''
st.code(code, language='python')

st.area_chart(data=age_hbp, x='age', y='platelets')


# Visualize data with line chart
st.subheader('Line Plot')
st.text('Below is the data visualized in a line plot')
age_hbp = data[['age', 'platelets']]
st.line_chart(data=age_hbp, x='age', y='platelets')