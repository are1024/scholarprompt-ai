import sys
from pathlib import Path

# اضافه کردن پوشه اصلی پروژه به مسیر پایتون
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import streamlit as st
from src.presentation.styles.custom_css import apply_custom_css
from src.presentation.components.sidebar import render_sidebar
from src.presentation.pages.create_prompt import render_create_prompt_page

# تنظیمات اصلی صفحه Streamlit
st.set_page_config(
    page_title="ScholarPrompt-AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    # اعمال فونت و استایل سفارشی
    apply_custom_css()

    # رندر Sidebar و دریافت صفحه انتخاب‌شده
    selected_page = render_sidebar()

    # هدایت صفحات (Routing)
    if selected_page == "🚀 ساخت پرامپت جدید":
        render_create_prompt_page()
    elif selected_page == "📚 تاریخچه پرامپت‌ها":
        st.header("📚 تاریخچه پرامپت‌ها")
        st.info("بخش تاریخچه به زودی فراخوانی می‌شود.")
    elif selected_page == "📊 داشبورد کاربر":
        st.header("📊 داشبورد کاربر")
        st.info("بخش داشبورد و آمار به‌زودی فعال می‌شود.")

if __name__ == "__main__":
    main()
