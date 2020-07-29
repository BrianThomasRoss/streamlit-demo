import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import streamlit as st

st.title('Classify iris flower species')

# Load data
iris = load_iris(as_frame=True)
df = iris.data
df['species'] = iris.target

# Wrangle data
numbered_names = dict(enumerate(iris.target_names))
df['species'] = df['species'].map(numbered_names)

# Fit model
@st.cache(persist=True)
def fit_model(df):
    features = ['petal width (cm)', 'petal length (cm)']
    target = 'species'
    model = LogisticRegression()
    model.fit(df[features], df[target])
    return model

model = fit_model(df)

# Get inputs
st.markdown("""
## What are the flower's measurements?
""")
petal_width = st.slider('Petal width (cm)', min_value=0.1, max_value=2.5, value=1.20)
petal_length = st.slider('Petal length (cm)', min_value=1.0, max_value=6.9, value=3.76)

# Make predictions
st.markdown("""
## Prediction
""")
X_new = [[petal_width, petal_length]]
y_pred = model.predict(X_new)[0]

# Visualize
st.markdown(f"""
We predict the flower is **{y_pred}**, using our logistic regression model.

The grey point represents the flower we're predicting. The colored points are from our training data. 
""")
ax = plt.gca()
sns.scatterplot(x='petal width (cm)', y='petal length (cm)', hue='species', alpha=0.5, data=df, ax=ax)
ax.scatter(x=petal_width, y=petal_length, c='grey')
st.pyplot()

# Show data
st.markdown("""
## Data
""")
st.dataframe(df)
