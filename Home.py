import streamlit as st
import os

st.set_page_config(
    page_title="Home",
    page_icon="👋",
    initial_sidebar_state="collapsed"
)

st.write("# Welcome to App! 👋")


st.markdown(
    """
    This app generate the test cases in Standard BDD format using OpenAI

    **👈 There are two links provided below:\n
    [Get Documents](http://localhost:8501/page1): This link is used to get or search documents. You can 
                                                     copy the text and paste it directly in Generate Test Cases
                                                    page as earlier or new requirements. 

    [Generate Test Cases](http://localhost:8501/page2): This link will navigate you to Test cases page where
                         you can paste/ type earlier and new requirements and accordingly
                         test cases will be generated in standard BDD format.
   
"""
)
