import streamlit as st

def apply_custom_css():
    st.markdown("""
        <style>
        @import url('https://cdn.jsdelivr.net/gh/rastikerdar/vazirmatn@v33.003/Vazirmatn-font-face.css');

        /* ۱. اعمال فونت و راست‌چین کردن */
        html, body, [class*="css"], p, h1, h2, h3, h4, h5, h6, span, label, input, textarea, button {
            font-family: 'Vazirmatn', sans-serif !important;
        }

        .main, .stApp {
            direction: rtl;
            text-align: right;
        }

        /* ۲. مخفی کردن کامل دکمه باز/بسته کردن Sidebar (ثابت ساختن منو) */
        [data-testid="stSidebarCollapseButton"],
        [data-testid="stSidebarExpandButton"],
        button[aria-label="Close sidebar"],
        button[aria-label="Open sidebar"] {
            display: none !important;
        }

        /* ۳. قفل کردن عرض Sidebar و جلوگیری از تغییر سایز */
        [data-testid="stSidebar"] {
            min-width: 280px !important;
            max-width: 280px !important;
        }

        /* ۴. حل مشکل تداخل Placeholder و ورودی‌ها */
        .stTextInput input, .stTextArea textarea {
            direction: rtl !important;
            text-align: right !important;
        }

        /* ۵. چپ‌به-راست نگه‌داشتن باکس‌های کد پرامپت */
        .stCodeBlock, div[data-testid="stCodeBlock"] {
            direction: ltr !important;
            text-align: left !important;
        }

        /* ۶. حذف اسکرول افقی ناخواسته */
        .main .block-container {
            overflow-x: hidden !important;
            padding-top: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)
