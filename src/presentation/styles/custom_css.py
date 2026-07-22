import streamlit as st

def apply_custom_css():
    st.markdown("""
        <style>
        /* ۱. فونت و جهت کلی صفحه */
        @import url('https://cdn.jsdelivr.net/gh/rastikerdar/vazirmatn@v33.003/Vazirmatn-font-face.css');

        html, body, [class*="css"] {
            font-family: 'Vazirmatn', sans-serif !important;
            direction: rtl;
            text-align: right;
        }

        /* ۲. اصلاح مشکل دکمه باز/بسته کردن Sidebar و متن آیکون‌ها */
        [data-testid="stSidebarCollapseButton"] button span,
        [data-testid="stSidebarExpandButton"] button span {
            font-family: sans-serif !important; /* جلوگیری از بهم‌ریختگی آیکون‌های متنی */
            direction: ltr !important;
        }

        [data-testid="stSidebarCollapseButton"], 
        [data-testid="stSidebarExpandButton"] {
            overflow: visible !important;
            white-space: nowrap !important;
        }

        /* ۳. حل مشکل تداخل Placeholder با متن ورودی‌ها (Input & Textarea) */
        .stTextInput input, .stTextArea textarea {
            direction: rtl !important;
            text-align: right !important;
            font-family: 'Vazirmatn', sans-serif !important;
        }

        /* تنظیم رنگ و رفتار Placeholder */
        .stTextInput input::placeholder, .stTextArea textarea::placeholder {
            text-align: right !important;
            direction: rtl !important;
            opacity: 0.6;
            color: #888888;
        }

        /* ۴. حذف نوار پیمایش (Scrollbar) اضافی و اسکرول‌های ناخواسته افقی */
        .main .block-container {
            overflow-x: hidden !important;
            padding-top: 2rem;
            padding-bottom: 2rem;
        }

        body {
            overflow-x: hidden !important;
        }

        /* ۵. استایل اختصاصی باکس کد (برای نمایش صحیح پرامپت‌ها) */
        .stCodeBlock, div[data-baseweb="textarea"] {
            direction: ltr !important;
            text-align: left !important;
        }
        
        /* اصلاح دکمه‌های اصلی */
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
        </style>
    """, unsafe_allow_html=True)
