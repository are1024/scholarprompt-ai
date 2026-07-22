import streamlit as st

def apply_custom_css():
    st.markdown("""
        <style>
        @import url('https://cdn.jsdelivr.net/gh/rastikerdar/vazirmatn@v33.003/Vazirmatn-font-face.css');

        /* ۱. فونت و جهت کلی */
        html, body, [class*="css"], div, h1, h2, h3, h4, h5, h6, p, span, button, input {
            font-family: 'Vazirmatn', sans-serif !important;
            direction: rtl;
            text-align: right;
        }

        /* ۲. اصلاح رنگ پس‌زمینه اصلی در حالت Light Mode */
        .stApp {
            background-color: #F8FAFC !important; /* پس‌زمینه اصلی خاکستری ملایم */
            color: #0F172A !important;
        }

        /* ۳. قفل کردن عرض Sidebar و استایل متمایز آن */
        [data-testid="stSidebarCollapseButton"],
        [data-testid="stSidebarExpandButton"],
        button[aria-label="Close sidebar"],
        button[aria-label="Open sidebar"] {
            display: none !important;
        }

        [data-testid="stSidebar"] {
            min-width: 290px !important;
            max-width: 290px !important;
            background-color: #FFFFFF !important;
            border-left: 1px solid #E2E8F0 !important;
            box-shadow: -2px 0 10px rgba(0, 0, 0, 0.02);
        }

        .main .block-container {
            overflow-x: hidden !important;
            padding-top: 2rem;
            max-width: 1100px;
        }

        /* ۴. استایل باکس‌های ورودی (Inputs & Textareas) */
        .stTextInput input, .stTextArea textarea, .stSelectbox > div > div {
            background-color: #FFFFFF !important;
            color: #0F172A !important;
            direction: rtl !important;
            text-align: right !important;
            border-radius: 8px !important;
            border: 1px solid #CBD5E1 !important;
            box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05) !important;
        }

        .stTextInput input:focus, .stTextArea textarea:focus {
            border-color: #2563EB !important;
            box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15) !important;
        }

        /* ۵. حذف متون راهنمای زیر ورودی‌ها */
        [data-testid="stInputInstruction"],
        [data-testid="InputInstructions"],
        .stTextInput small,
        .stTextArea small,
        div[data-baseweb="typo-caption"] {
            display: none !important;
            visibility: hidden !important;
            height: 0px !important;
            margin: 0px !important;
            padding: 0px !important;
        }

        /* ۶. دکمه‌های اصلی (Primary Buttons) */
        .stButton>button {
            width: 100%;
            background-color: #2563EB !important;
            color: #FFFFFF !important;
            border-radius: 8px !important;
            font-weight: 600 !important;
            padding: 0.6rem 1rem !important;
            border: none !important;
            transition: all 0.2s ease-in-out !important;
            box-shadow: 0 2px 4px rgba(37, 99, 235, 0.2) !important;
        }

        .stButton>button:hover {
            background-color: #1D4ED8 !important;
            box-shadow: 0 4px 8px rgba(29, 78, 216, 0.3) !important;
            transform: translateY(-1px);
        }

        /* ۷. باکس خروجی کدهای پرامپت (Prompt Output Box) */
        .stCodeBlock {
            direction: ltr !important;
            text-align: left !important;
            background-color: #0F172A !important; /* پس‌زمینه تیره برای کنتراست بالای پرامپت */
            color: #F8FAFC !important;
            border-radius: 10px !important;
            border: 1px solid #334155 !important;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1) !important;
        }

        /* ۸. استایل Expander و کارت‌ها */
        .streamlit-expanderHeader {
            background-color: #FFFFFF !important;
            border-radius: 8px !important;
            border: 1px solid #E2E8F0 !important;
            color: #1E293B !important;
            font-weight: 600 !important;
        }

        /* ۹. کارت‌های آماری (Metrics) */
        [data-testid="stMetric"] {
            background-color: #FFFFFF !important;
            padding: 1rem !important;
            border-radius: 10px !important;
            border: 1px solid #E2E8F0 !important;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05) !important;
        }

        [data-testid="stMetricValue"] {
            font-size: 1.8rem !important;
            color: #2563EB !important;
            font-weight: bold !important;
        }

        [data-testid="stMetricLabel"] {
            font-size: 0.9rem !important;
            color: #64748B !important;
        }
        </style>
    """, unsafe_allow_html=True)
