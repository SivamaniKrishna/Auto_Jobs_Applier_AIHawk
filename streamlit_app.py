# app.py

import streamlit as st
from datetime import datetime
from main import main  # Import the function from main.py

st.title("Execute main.py Function App")

# Button to execute main.py functionality
if st.button("Click to Execute main.py"):
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.write(f"Execution started at: {start_time}")
    
    # Run the main.py function
    try:
        run_main()  # This calls the main function in main.py
        st.success("main.py executed successfully!")
        
        end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.write(f"Execution completed at: {end_time}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
