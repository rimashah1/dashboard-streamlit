import streamlit as st
import pandas as pd
import numpy as np

DATA_URL = ('https://raw.githubusercontent.com/sauravmishra1710/Heart-Failure-Condition-And-Survival-Analysis/master/Data/heart_failure_clinical_records_dataset.csv')

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

# Load 10,000 rows of data into the dataframe.
data = load_data(10000)

st.title('Heart Failure Data')

st.subheader('Raw data')
st.write(data)

st.text('Below is the code to visualize a histogram')

code = '''
        hist_values = np.histogram(data['age'], bins = 10)
        st.bar_chart(hist_values)
        '''
st.code(code, language='python')

hist_values = np.histogram(data['age'], bins = 10)
st.bar_chart(hist_values)

st.text('Below is the data to be visualized in a scatter plot')
age_hbp = data[['age', 'high_blood_pressure']]

st.line_chart(data=age_hbp, x='age', y='high_blood_pressure')