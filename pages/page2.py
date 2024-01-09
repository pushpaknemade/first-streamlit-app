import streamlit as st
import time

with st.status("Authentication please wait...") as s:
    time.sleep(6)
    s.update(label="done", expanded=True)
    st.write("Thank you...")