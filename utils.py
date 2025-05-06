from tempfile import NamedTemporaryFile
import streamlit as st
import re

def file_upload(uploaded_file):
            
    # If file is uploaded
    if uploaded_file is not None:
        file_name = uploaded_file.name
        with NamedTemporaryFile(dir='.') as f:
            # regex to get all the text but whatever is after the last "\"
            f2 = re.search(r'(.*)\\', f.name).group(1)
    
            # Return the file path
            return (f2, f2 + '\\' + file_name)