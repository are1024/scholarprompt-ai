import sys
from pathlib import Path

# تنظیم مسیر اصلی پروژه
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import streamlit as st
from streamlit_cookies_controller import CookieController
from src.presentation.styles.custom_css import apply_custom_css
from src.presentation.components.sidebar import render_sidebar
from src.presentation.pages.create_prompt import render_create_prompt_page
from src.presentation.pages.history import render_history_page
from src.presentation.pages.dashboard import render_dashboard_page
from src.infrastructure.database.supabase_client import SupabaseManager  # ایمپورت مدیریت سوپابیس

st.set_page_config(
    page_title="ScholarPrompt-AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"  # منو همیشه در ابتدا باز است
)


def main():
    apply_custom_css()
    supabase = SupabaseManager.get_client()
    
    # راه‌اندازی کنترلر کوکی
    cookie_controller = CookieController()

    # بررسی و حفظ وضعیت لاگین کاربر (ترکیب URL و کوکی برای پایداری صددرصدی)
    if "user" not in st.session_state or st.session_state["user"] is None:
        # ۱. اولویت اول: بررسی URL (برای رفرش آنی با F5 بدون تاخیر کوکی)
        refresh_token = st.query_params.get("rt")
        
        # ۲. اگر در URL نبود، خواندن توکن از کوکی مرورگر (برای وقتی که مرورگر بسته شده بوده)
        if not refresh_token:
            try:
                refresh_token = cookie_controller.get('refresh_token')
            except Exception:
                pass
        
        if refresh_token:
            try:
                # تلاش برای بازیابی سشن با استفاده از توکن
                response = supabase.auth.refresh_session(refresh_token)
                if response.user:
                    st.session_state["user"] = response.user
                    # آپدیت کردن همزمان کوکی و URL با توکن جدید
                    if response.session and response.session.refresh_token:
                        new_token = response.session.refresh_token
                        st.query_params["rt"] = new_token
                        try:
                            cookie_controller.set('refresh_token', new_token, max_age=30*24*60*60)
                        except Exception:
                            pass
            except Exception:
                # اگر توکن نامعتبر یا منقضی بود، پاکسازی کامل از URL و کوکی
                if "rt" in st.query_params:
                    del st.query_params["rt"]
                try:
                    cookie_controller.remove('refresh_token')
                except Exception:
                    pass

    selected_page = render_sidebar()

    if selected_page == "🚀 ساخت پرامپت جدید":
        render_create_prompt_page()
    elif selected_page == "📚 تاریخچه پرامپت‌ها":
        render_history_page()
    elif selected_page == "📊 داشبورد کاربر":
        render_dashboard_page()

if __name__ == "__main__":
    main()