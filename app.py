#Importing the library
import streamlit as st
from propt_engine import run_prompt

#creating a Streamlit Page
st.set_page_config(page_title = "Prompt Engineering App",layout = "centered" )
st.title("Prompt Engineering APP")

#prompt types dropdown
prompt_type = [ 
    "Zero-Shot",
    "Few_Shot",
    "Instruction-Based",
    "Chain-of-Thought",
    "Role-Based"
]

selected_prompt = st.selectbox("Choose Prompt Type:",prompt_type)
user_input = st.text_area("Enter your prompt over here:",height = 150)

if st.button("Generate the Content"):
    with st.spinner("Generating Content........."):
        output = run_prompt(selected_prompt,user_input)
    st.markdown("Response: ")
    st.code(output)