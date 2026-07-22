import streamlit as st

def apply_custom_css():
    st.markdown("""
        <style>
        @import url('https://cdn.jsdelivr.net/gh/rastikerdar/vazirmatn@v33.003/Vazirmatn-font-face.css');

        /* ۱. فونت کلی و جهت صفحه */
        html, body, [class*="css"], div, h1, h2, h3, h4, h5, h6, p, span, button, input {
            font-family: 'Vazirmatn', sans-serif !important;
            direction: rtl;
            text-align: right;
        }

        /* ۲. مخفی کردن دکمه باز/بسته شدن منو جهت ثابت ماندن Sidebar */
        [data-testid="stSidebarCollapseButton"],
        [data-testid="stSidebarExpandButton"],
        button[aria-label="Close sidebar"],
        button[aria-label="Open sidebar"] {
            display: none !important;
        }

        /* ۳. قفل کردن عرض Sidebar */
        [data-testid="stSidebar"] {
            min-width: 290px !important;
            max-width: 290px !important;
            background-color: #F8FAFC !important;
            border-left: 1px solid #E2E8F0;
        }

        .main .block-container {
            overflow-x: hidden !important;
            padding-top: 2.5rem;
        }

        /* ۴. افزایش ارتفاع و پدینگ ورودی‌ها */
        .stTextInput input {
            height: 50px !important; /* افزایش ارتفاع ورودی تک‌خطی */
            padding: 10px 14px !important;
            direction: rtl !important;
            text-align: right !important;
            border-radius: 8px !important;
            border: 1px solid #CBD5E1 !important;
            font-size: 0.95rem !important;
        }

        .stTextArea textarea {
            min-height: 120px !important; /* افزایش ارتفاع ورودی چندخطی */
            padding: 12px 14px !important;
            direction: rtl !important;
            text-align: right !important;
            border-radius: 8px !important;
            border: 1px solid #CBD5E1 !important;
            font-size: 0.95rem !important;
        }

        .stTextInput input:focus, .stTextArea textarea:focus {
            border-color: #2563EB !important;
            box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.2) !important;
        }

        /* ۵. حذف کامل متن‌های راهنمای پیش‌فرض و Placeholderهای مزاحم Streamlit */
        [data-testid="stInputInstruction"], 
        .stTextInput small, 
        .stTextArea small {
            display: none !important; /* مخفی کردن متن Press Enter to apply */
        }

        /* مخفی کردن Placeholderهای درون باکس در صورت نیاز */
        ::placeholder {
            color: transparent !important; /* شفاف کردن متن Placeholder داخل باکس */
        }

        /* ۶. دکمه‌های اصلی */
        .stButton>button {
            width: 100%;
            background-color: #2563EB;
            color: white;
            border-radius: 8px;
            font-weight: bold;
            padding: 0.6rem 1rem;
            border: none;
            transition: all 0.3s ease;
            box-shadow: 0 2px 4px rgba(37, 99, 235, 0.2);
        }

        .stButton>button:hover {
            background-color: #1D4ED8;
            border-color: #1D4ED8;
            color: white;
            box-shadow: 0 4px 6px rgba(29, 78, 216, 0.3);
        }

        /* ۷. باکس کدهای پرامپت */
        .stCodeBlock {
            direction: ltr !important;
            text-align: left !important;
            border-radius: 10px !important;
            border: 1px solid #E2E8F0 !important;
        }

        /* ۸. کارت‌های آماری (Metrics) */
        [data-testid="stMetricValue"] {
            font-size: 1.8rem !important;
            color: #2563EB !important;
            font-weight: bold !important;
        }
        
        [data-testid="stMetricLabel"] {
            font-size: 0.95rem !important;
            color: #64748B !important;
        }
        </style>
    """, unsafe_allow_html=True)
