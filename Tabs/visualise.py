"""This modules contains data about visualisation page"""

# Import necessary modules
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
'''from sklearn.metrics import plot_confusion_matrix'''
from sklearn import tree
import streamlit as st


# Import necessary functions from web_functions
from web_functions import train_model

def app(df, X, y):
    """This function create the visualisation page"""
    
    # Remove the warnings
    warnings.filterwarnings('ignore')
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Set the page title
    st.title("Visualise Flood Effect Demographics")

    # Create a checkbox to show correlation heatmap
    if st.checkbox("Show the correlation heatmap"):
        st.subheader("Correlation Heatmap")

        fig = plt.figure(figsize = (15, 7))
        ax = sns.heatmap(df.iloc[:, 1:].corr(), annot = True)   # Creating an object of seaborn axis and storing it in 'ax' variable
        bottom, top = ax.get_ylim()                             # Getting the top and bottom margin limits.
        ax.set_ylim(bottom + 0.5, top - 0.5)                    # Increasing the bottom and decreasing the top margins respectively.
        st.pyplot(fig)
        
    if st.checkbox("Show the flood chances from prevelant factors"):
        st.subheader("Flood Chances")
        fig = plt.figure(figsize = (15, 7))
        fig, ax = plt.subplots()

        color1 = st.sidebar.color_picker("Select Color for Dataset 1", "#2596be")
        color2 = st.sidebar.color_picker("Select Color for Dataset 2", "#2596be")
        color3 = st.sidebar.color_picker("Select Color for Dataset 3", "#2596be")
        color4 = st.sidebar.color_picker("Select Color for Dataset 4", "#2596be")
        
        
        ax.hist(df['ClimateChange'], bins=30, alpha=0.5, color=color1, label='ClimateChange')
        ax.hist(df['DrainageSystems'], bins=30, alpha=0.5, color=color2, label='DrainageSystems')
        ax.hist(df['IneffectiveDisasterPreparedness'], bins=30, alpha=0.5, color=color3, label='IneffectiveDisasterPreparedness')
        ax.hist(df['Deforestation'], bins=30, alpha=0.5, color=color4, label='Deforestation')
        ax.legend()
        st.pyplot(plt)
        
    

  

    
