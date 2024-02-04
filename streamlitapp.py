import streamlit as st
import matplotlib.pyplot as plt

def run_app(kmeans_clustering_func):
    st.title("Deforestation Detection")

    uploaded_file = st.file_uploader("Choose an image...", type=['jpg','png','jpeg','pdf'])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)

        segmented_image, fig = kmeans_clustering_func(uploaded_file)

        st.image(segmented_image, caption="Segmented Image.", use_column_width=True)

        st.pyplot(fig)
