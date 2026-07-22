import streamlit as st

def apply_custom_css():
    st.markdown("""
        <style>
        @import url('https://cdn.jsdelivr.net/gh/rastikerdar/vazirmatn@v33.003/Vazirmatn-font-face.css');

        /* ۱. تنظیمات عمومی فونت و جهت */
        html, body, [class*="css"], div, h1, h2, h3, h4, h5, h6, p, span, button, input {
            font-family: 'Vazirmatn', sans-serif !important;
            direction: rtl;
            text-align: right;
        }

        /* ۲. قفل کردن عرض Sidebar */
        [data-testid="stSidebarCollapseButton"],
        [data-testid="stSidebarExpandButton"],
        button[aria-label="Close sidebar"],
        button[aria-label="Open sidebar"] {
            display: none !important;
        }

        [data-testid="stSidebar"] {
            min-width: 290px !important;
            max-width: 290px !important;
        }

        .main .block-container {
            overflow-x: hidden !important;
            padding-top: 2rem;
            max-width: 1100px;
        }

        /* ۳. حذف متون راهنمای زیر ورودی‌ها */
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

        /* ۴. اجبار دکمه Primary به رنگ سبز کم‌رنگ (با اضافه کردن Selector دقیق‌تر) */
        div.stButton > button[kind="primary"],
        div.stButton > button[data-testid="baseButton-primary"] {
            width: 100% !important;
            background-color: #DCFCE7 !important; /* سبز کم‌رنگ */
            color: #166534 !important; /* متن سبز تیره */
            border: 1px solid #86EFAC !important;
            border-radius: 8px !important;
            font-weight: 700 !important;
            padding: 0.6rem 1rem !important;
            transition: all 0.2s ease-in-out !important;
            box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05) !important;
        }

        div.stButton > button[kind="primary"]:hover,
        div.stButton > button[data-testid="baseButton-primary"]:hover {
            background-color: #BBF7D0 !important; /* سبز کمی پررنگ‌تر */
            border-color: #4ADE80 !important;
            color: #14532D !important;
            transform: translateY(-1px);
        }

        /* ۵. استایل‌های حالت Light Mode برای کنتراست مناسب */
        @media (prefers-color-scheme: light) {
            .stApp {
                background-color: #F1F5F9 !important;
                color: #0F172A !important;
            }

            [data-testid="stSidebar"] {
                background-color: #FFFFFF !important;
                border-left: 1px solid #E2E8F0 !important;
            }

            .stTextInput input, .stTextArea textarea, .stSelectbox > div > div {
                background-color: #FFFFFF !important;
                color: #0F172A !important;
                border: 1px solid #CBD5E1 !important;
                border-radius: 8px !important;
            }

            [data-testid="stMetric"] {
                background-color: #FFFFFF !important;
                border: 1px solid #E2E8F0 !important;
                border-radius: 10px !important;
            }

            .streamlit-expanderHeader {
                background-color: #FFFFFF !important;
                border: 1px solid #E2E8F0 !important;
                border-radius: 8px !important;
            }

            .stCodeBlock {
                background-color: #1E293B !important;
                border: 1px solid #334155 !important;
                border-radius: 8px !important;
            }
        }
        </style>
    """, unsafe_allow_html=True)
