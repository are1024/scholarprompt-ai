import streamlit as st

def apply_custom_css():
    st.markdown("""
        <style>
        /* ۱. اعمال فونت فقط به عناصر متنی (جلوگیری از تغییر فونت آیکون‌ها) */
        @import url('https://cdn.jsdelivr.net/gh/rastikerdar/vazirmatn@v33.003/Vazirmatn-font-face.css');

        p, h1, h2, h3, h4, h5, h6, span, label, input, textarea, button {
            font-family: 'Vazirmatn', sans-serif;
        }

        /* ۲. استثنا کردن آیکون‌های متنی Streamlit جهت جلوگیری از نمایش متن نام آیکون */
        .material-symbols-rounded, 
        [data-testid="stIcon"],
        [class*="st-"] i,
        [data-testid="stSidebarCollapseButton"] *,
        [data-testid="stSidebarExpandButton"] * {
            font-family: 'Material Symbols Rounded', sans-serif !important;
        }

        /* ۳. راست‌چین کردن کل بدنه و حذف اسکرول افقی ناخواسته */
        .main, .stApp {
            direction: rtl;
            text-align: right;
        }

        .main .block-container {
            max-width: 95%;
            padding-top: 2rem;
            overflow-x: hidden;
        }

        /* ۴. حل مشکل تداخل Placeholder با متن تایپ‌شده در Inputها */
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea {
            direction: rtl !important;
            text-align: right !important;
        }

        /* ۵. نگه داشتن باکس‌های کد به‌صورت چپ‌به-راست (LTR) برای خوانایی پرامپت‌ها */
        .stCodeBlock, div[data-testid="stCodeBlock"] {
            direction: ltr !important;
            text-align: left !important;
        }
        </style>
    """, unsafe_allow_html=True)
