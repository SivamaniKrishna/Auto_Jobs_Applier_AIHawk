import streamlit as st
import subprocess
from datetime import datetime

st.title("Command Execution App")

# Display a button to run commands
if st.button("Click to Execute Commands"):
    try:
        # Run the first command: install requirements
        st.write("Installing requirements...")
        install_output = subprocess.run(
            ["pip", "install", "-r", "requirements.txt"], 
            capture_output=True, text=True
        )
        st.code(install_output.stdout)  # Display the output of the installation

        # Run the second command: execute the script
        st.write("Executing main.py...")
        exec_output = subprocess.run(
            ["python", "main.py"], 
            capture_output=True, text=True
        )
        st.code(exec_output.stdout)  # Display the output of the script execution

        # Show the time when execution completed
        execution_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.success(f"Execution completed at: {execution_time}")

    except Exception as e:
        st.error(f"An error occurred: {e}")
