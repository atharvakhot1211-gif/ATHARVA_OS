import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        /* Main Background */
        .stApp { background-color: #FFFFFF; }
        
        /* Text and Headers */
        h1, h2, h3, p, span, label { 
            color: #1A1A1A !important; 
            font-family: 'Inter', sans-serif; 
        }
        
        /* Clean Containers */
        div[data-testid="stVerticalBlock"] { 
            background-color: #FFFFFF; 
            border-radius: 10px; 
        }
        
        /* Buttons - Minimalist White */
        .stButton>button {
            border-radius: 8px; 
            border: 1px solid #E0E0E0;
            background-color: #FFFFFF; 
            color: #1A1A1A; 
            transition: 0.3s;
        }
        .stButton>button:hover { 
            border-color: #000000; 
            background-color: #F9F9F9; 
        }
        </style>
    """, unsafe_allow_html=True)