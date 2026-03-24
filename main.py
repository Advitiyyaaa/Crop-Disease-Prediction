import streamlit as st
import tensorflow as tf
import numpy as np
page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background-image: url(https://wallpapercave.com/wp/wp9212357.jpg);
background-size: cover;

}
</style>
"""
st.markdown(
        """
        <style>
        body {
            background-color: #ADD8E6; /* Light blue background */
            color: black; /* Black text color */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

st.markdown(page_bg_img, unsafe_allow_html=True)

#Tensorflow Model Prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model("trained_plant_disease_model.keras")
    image = tf.keras.preprocessing.image.load_img(test_image,target_size=(128,128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr]) 
    predictions = model.predict(input_arr)
    return np.argmax(predictions) 

#Sidebar

st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page",["Home","About","Disease Recognition"])

#Main Page
if(app_mode=="Home"):
    st.markdown(
    """
    <h1 style="
        color: black; 
        text-shadow: 0 0 10px rgba(173, 216, 230, 0.8), 
                     0 0 20px rgba(173, 216, 230, 0.6), 
                     0 0 30px rgba(173, 216, 230, 0.4);
    ">
        ScareCrowAI
    </h1>
    """,
    unsafe_allow_html=True
)
    #image_path = "home_page.jpeg"
    #st.image(image_path,use_column_width=True)
    st.markdown(
        """
        <div style="color: black;">
    Welcome to the Crop Disease Recognition System! 🌿🔍
    
    Our mission is to help in identifying crop diseases efficiently. Upload an image of a plant, and our system will analyze it to detect any signs of diseases. Together, let's protect our crops and ensure a healthier harvest!

    <h3 style="color: black;">How it works?</h3>
    <p>1. <b>Upload Image:</b> Go to the <b>Disease Recognition</b> page and upload an image of a plant with suspected diseases.<p>
    <p>2. <b>Analysis:</b> Our system will process the image using advanced algorithms to identify potential diseases.<p>
    <p>3. <b>Results:</b> View the results and recommendations for further action.<p>

    <h3 style="color: black;">Why Choose Us?</h3> 
    <p>- <b>Accuracy:</b> Our system utilizes state-of-the-art machine learning techniques for accurate disease detection.<p>
    <p>- <b>User-Friendly:</b> Simple and intuitive interface for seamless user experience.<p>
    <p>- <b>Fast and Efficient:</b> Receive results in seconds, allowing for quick decision-making.<p>

    <h3 style="color: black;">Get Started</h3>
    <p>Click on the <b>Disease Recognition</b> page in the sidebar to upload an image and experience the power of our Plant Disease Recognition System!<p>

    <h3 style="color: black;">About Us</h3> 
    <p>Learn more about the project, our team, and our goals on the <b>About</b> page.<p>
    """,
    unsafe_allow_html=True
    )

#About Project
elif(app_mode=="About"):
    #st.header("<h3 style="color: black;">About</h3>")
    st.markdown(
        """
    <h2 style="color: black;">About</h2>
        <div style="color: black;">
    <h3 style="color: black;">About Us</h3>
    <p><b>Team Name - ScareCrow</b><p>
    <p><b>Product Name - ScareCrowAI</b><p>
    <h3 style="color: black;">About Dataset</h3>
    This dataset has been recreated using offline augmentation techniques applied to the original dataset.It contains approximately 87,000 RGB images of both healthy and diseased crop leaves, categorized into 38 distinct classes. To facilitate model training and evaluation, the dataset is split into training and validation sets in an 80/20 ratio, while maintaining the original directory structure.

Additionally, a separate directory has been created, containing 33 test images specifically for prediction purposes.e.

   
    """,
    unsafe_allow_html=True
    )

#Prediction Page
elif(app_mode=="Disease Recognition"):
    #st.header("Disease Recognition")
    st.markdown(
    """
    <style>
    .header {
        color: black;
        font-size: 36px;
        font-weight: bold;
    }
    </style>
    <h1 class="header">Disease Recognition</h1>
    """,
    unsafe_allow_html=True
)
    
    test_image = st.file_uploader("")
    if(st.button("Show Image")):
        st.image(test_image,width=4,use_column_width=True)
    #Predict button
    if(st.button("Predict")):
        st.spinner()
        st.write("Our Prediction")
        result_index = model_prediction(test_image)
        #Reading Labels
        class_name = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
                    'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 
                    'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 
                    'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 
                    'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 
                    'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
                    'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 
                    'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 
                    'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 
                    'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 
                    'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 
                    'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 
                    'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
                      'Tomato___healthy']
        st.success("Model is Predicting it's a {}".format(class_name[result_index]))
