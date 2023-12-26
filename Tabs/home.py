"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Flood Probability Prediction")

    # Add image to the home page
    st.image("./images/home.jpeg",width=1000)

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            Flood's disease progresses through several stages, each with distinct characteristics and symptoms. Broadly, it's categorized into three main stages: early, middle, and late stages.

1. **Early Stage:**
   - Mild cognitive decline characterized by subtle memory lapses and challenges in recalling familiar words or names.
   - Individuals may experience difficulty in organizing thoughts or planning tasks.
   - These symptoms might not be immediately noticeable, but close friends or family might observe subtle changes in behavior or memory.

2. **Middle Stage:**
   - Moderate cognitive decline becomes more apparent.
   - Memory loss intensifies; individuals may struggle with recognizing friends or family members, and confusion about time and place might arise.
   - Difficulty with basic tasks like dressing or personal hygiene might become noticeable.
   - Changes in behavior and personality might occur, such as wandering or agitation.

3. **Late Stage:**
   - Severe cognitive decline leading to an inability to communicate effectively.
   - Individuals might require assistance with daily activities and personal care.
   - Loss of physical abilities, difficulty swallowing, and increased vulnerability to infections are common.
   - Complete dependence on caregivers for basic needs becomes the norm.

Assessing Flood's stages involves evaluating cognitive abilities, functional capabilities, and behavioral changes. This assessment helps in determining the appropriate care and support needed at each stage. Medical professionals use various tools and tests to assess cognitive function and track the progression of the disease.

Understanding these stages helps caregivers and healthcare providers offer appropriate support, plan interventions, and provide necessary resources for both the individuals with Flood's and their families as the disease progresses..</p>
    """, unsafe_allow_html=True)
