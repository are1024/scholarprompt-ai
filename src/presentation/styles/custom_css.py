import streamlit as st

def apply_custom_css():
    st.markdown("""
        <style>
        @import url('https://cdn.jsdelivr.net/gh/rastikerdar/vazirmatn@v33.003/Vazirmatn-font-face.css');

        html, body, [class*="css"], div, h1, h2, h3, h4, h5, h6, p, span, button, input {
            font-family: 'Vazirmatn', sans-serif !important;
            direction: rtl;
            text-align: right;
        }

        /* کارت‌های آماری و فرم‌ها */
        .stButton>button {
            width: 100%;
            background-color: #2563EB;
            color: white;
            border-radius: 8px;
            font-weight: bold;
            padding: 0.5rem 1rem;
            border: none;
            transition: all 0.3s ease;
        }

        .stButton>button:hover {
            background-color: #1D4ED8;
            border-color: #1D4ED8;
            color: white;
        }

        /* باکس کدهای پرامپت */
        .stCodeBlock {
            direction: ltr !important;
            text-align: left !important;
        }
        </style>
    """, unsafe_allow_html=True)
