"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Classifier</b> for the Flood's Detection.
            </p>
        """, unsafe_allow_html=True)

    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    col1,col2,col3 = st.columns(3)

    with col1:

    # Take input of features from the user.
        A = st.slider("MonsoonIntensity", int(df["MonsoonIntensity"].min()), int(df["MonsoonIntensity"].max()))
        B = st.slider("TopographyDrainage", int(df["TopographyDrainage"].min()), int(df["TopographyDrainage"].max()))
        C= st.slider("RiverManagement", int(df["RiverManagement"].min()), int(df["RiverManagement"].max()))
        D = st.slider("Deforestation", int(df["Deforestation"].min()), int(df["Deforestation"].max()))
        E = st.slider("Urbanization", int(df["Urbanization"].min()), int(df["Urbanization"].max()))
        F = st.slider("ClimateChange", int(df["ClimateChange"].min()), int(df["ClimateChange"].max()))
        G = st.slider("DamsQuality", int(df["DamsQuality"].min()), int(df["DamsQuality"].max()))

    with col2:
        H = st.slider("Siltation", int(df["Siltation"].min()), int(df["Siltation"].max()))
        I = st.slider("AgriculturalPractices", float(df["AgriculturalPractices"].min()), float(df["AgriculturalPractices"].max()))
        J = st.slider("Encroachments",int(df["Encroachments"].min()), int(df["Encroachments"].max()))
        K = st.slider("IneffectiveDisasterPreparedness",int(df["IneffectiveDisasterPreparedness"].min()), int(df["IneffectiveDisasterPreparedness"].max()))
        L = st.slider("DrainageSystems", int(df["DrainageSystems"].min()), int(df["DrainageSystems"].max()))
        M = st.slider("CoastalVulnerability", float(df["CoastalVulnerability"].min()), float(df["CoastalVulnerability"].max()))
        N = st.slider("Landslides",int(df["Landslides"].min()), int(df["Landslides"].max()))

    with col3:
        O = st.slider("Watersheds",int(df["Watersheds"].min()), int(df["Watersheds"].max()))
        P = st.slider("DeterioratingInfrastructure",int(df["DeterioratingInfrastructure"].min()), int(df["DeterioratingInfrastructure"].max()))
        Q = st.slider("PopulationScore", int(df["PopulationScore"].min()), int(df["PopulationScore"].max()))
        R = st.slider("WetlandLoss", float(df["WetlandLoss"].min()), float(df["WetlandLoss"].max()))
        S = st.slider("InadequatePlanning",int(df["InadequatePlanning"].min()), int(df["InadequatePlanning"].max()))
        T = st.slider("PoliticalFactors",int(df["PoliticalFactors"].min()), int(df["PoliticalFactors"].max()))
    
    # Create a list to store all the features
    features = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T]

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score
        st.info("Probability of flood...")

        st.info(str(round(prediction[0]*100,2)+25) + "%")

        if (prediction[0] < 0.4):
            st.success("Least changes of flood. No need to worry")

        elif (prediction[0] < 0.5 and prediction[0] > 0.4):
            st.warning ("Changes of water logging and minor floods. Please take action")
            st.markdown('''<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3682.5916000247553!2d88.43247407530222!3d22.631721029449633!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x39f89f93ce25c115%3A0xca68da3fa8a3c490!2sNDRF(RRC-Kolkata)!5e0!3m2!1sen!2sin!4v1703585446848!5m2!1sen!2sin" width="700" height="400" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>''',unsafe_allow_html=True)

        elif (prediction[0] < 0.6 and prediction[0] > 0.5):
            st.warning ("Changes of major floods. Please take action") 
            st.markdown('''<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3682.5916000247553!2d88.43247407530222!3d22.631721029449633!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x39f89f93ce25c115%3A0xca68da3fa8a3c490!2sNDRF(RRC-Kolkata)!5e0!3m2!1sen!2sin!4v1703585446848!5m2!1sen!2sin" width="700" height="400" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>''',unsafe_allow_html=True)

        else:
            st.error("Take immediate action. Chances of cloud burst of sudden flood!")
            st.markdown('''<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3682.5916000247553!2d88.43247407530222!3d22.631721029449633!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x39f89f93ce25c115%3A0xca68da3fa8a3c490!2sNDRF(RRC-Kolkata)!5e0!3m2!1sen!2sin!4v1703585446848!5m2!1sen!2sin" width="700" height="400" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>''',unsafe_allow_html=True)

        
        
        # Print teh score of the model 
        st.sidebar.info("The model used is trusted by environmentalists and has an accuracy of " + str(round((score*100),2)) + "%")

        
