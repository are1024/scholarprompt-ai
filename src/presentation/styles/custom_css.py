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

        /* ۱. مخفی کردن دکمه باز/بسته شدن منو جهت ثابت ماندن منوی سمت راست */
        [data-testid="stSidebarCollapseButton"],
        [data-testid="stSidebarExpandButton"],
        button[aria-label="Close sidebar"],
        button[aria-label="Open sidebar"] {
            display: none !important;
        }

        /* ۲. قفل کردن عرض منو و حذف اسکرول افقی ناخواسته */
        [data-testid="stSidebar"] {
            min-width: 280px !important;
            max-width: 280px !important;
        }

        .main .block-container {
            overflow-x: hidden !important;
        }

        /* ۳. اصلاح جهت ورودی‌ها برای جلوگیری از تداخل متن و Placeholder */
        .stTextInput input, .stTextArea textarea {
            direction: rtl !important;
            text-align: right !important;
        }

        /* ۴. حذف کامل و قطعی تمامی متن‌های راهنمای زیر ورودی‌ها */
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

        /* ۵. حذف و مخفی کردن متن‌های سیستمی آیکون‌های اکسپندر (مثل keyboard_arrow) */
        [data-testid="stExpander"] span span {
            font-size: 0 !important;
            color: transparent !important;
        }
        
        /* یا در صورت نیاز به حذف کلی آن بخش از آیکون */
        [data-testid="stExpander"] svg {
            /* تنظیمات آیکون در صورت نیاز */
        }
        </style>
    """, unsafe_allow_html=True)
