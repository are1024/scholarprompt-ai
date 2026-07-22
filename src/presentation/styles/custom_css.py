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

        /* ۲. قفل کردن عرض Sidebar و مخفی‌سازی دکمه باز/بستن */
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

        /* ۳. حذف متون راهنمای اضافه زیر ورودی‌ها */
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

        /* ۴. دکمه اصلی (تولید پرامپت) - سبز کم‌رنگ مدرن */
        .stButton>button {
            width: 100%;
            background-color: #DCFCE7 !important; /* سبز بسیار ملایم و شیک */
            color: #166534 !important; /* سبز تیره برای کنتراست متن */
            border: 1px solid #86EFAC !important;
            border-radius: 8px !important;
            font-weight: 700 !important;
            padding: 0.6.rem 1rem !important;
            transition: all 0.2s ease-in-out !important;
            box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05) !important;
        }

        .stButton>button:hover {
            background-color: #BBF7D0 !important; /* کمی پررنگ‌تر هنگام هور */
            border-color: #4ADE80 !important;
            color: #14532D !important;
            transform: translateY(-1px);
        }

        /* ========================================================= */
        /* ۵. استایل‌های اختصاصی برای حالت LIGHT MODE (تم روشن) */
        /* ========================================================= */
        @media (prefers-color-scheme: light) {
            /* پس‌زمینه اصلی صفحه: طوسی-آبی بسیار ملایم */
            .stApp {
                background-color: #F1F5F9 !important;
                color: #0F172A !important;
            }

            /* منوی سمت راست (Sidebar) */
            [data-testid="stSidebar"] {
                background-color: #FFFFFF !important;
                border-left: 1px solid #E2E8F0 !important;
            }

            /* ورودی‌های متنی و منوهای کشویی */
            .stTextInput input, .stTextArea textarea, .stSelectbox > div > div {
                background-color: #FFFFFF !important;
                color: #0F172A !important;
                border: 1px solid #CBD5E1 !important;
                border-radius: 8px !important;
            }

            .stTextInput input:focus, .stTextArea textarea:focus {
                border-color: #22C55E !important; /* فوکوس سبز ملایم */
                box-shadow: 0 0 0 3px rgba(34, 197, 94, 0.2) !important;
            }

            /* کارت‌های آماری */
            [data-testid="stMetric"] {
                background-color: #FFFFFF !important;
                border: 1px solid #E2E8F0 !important;
                border-radius: 10px !important;
                box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important;
            }

            /* آکاردئون‌ها (Expander) */
            .streamlit-expanderHeader {
                background-color: #FFFFFF !important;
                border: 1px solid #E2E8F0 !important;
                border-radius: 8px !important;
                color: #1E293B !important;
            }

            /* باکس کد نمایش پرامپت (تیره برای خوانایی بهتر) */
            .stCodeBlock {
                background-color: #1E293B !important;
                border: 1px solid #334155 !important;
                border-radius: 8px !important;
            }
        }
        </style>
    """, unsafe_allow_html=True)
