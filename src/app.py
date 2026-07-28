import sys
from pathlib import Path

# تنظیم مسیر اصلی پروژه
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import streamlit as st
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

    # بررسی و حفظ وضعیت لاگین کاربر هنگام رفرش صفحه با استفاده از URL (query_params)
    if "user" not in st.session_state or st.session_state["user"] is None:
        refresh_token = st.query_params.get("rt")
        
        if refresh_token:
            try:
                # تلاش برای بازیابی سشن با استفاده از توکن ذخیره شده در URL
                response = supabase.auth.refresh_session(refresh_token)
                if response.user:
                    st.session_state["user"] = response.user
                    # آپدیت کردن توکن جدید در URL اگر سشن تمدید شده باشد
                    if response.session and response.session.refresh_token:
                        st.query_params["rt"] = response.session.refresh_token
            except Exception:
                # اگر توکن نامعتبر یا منقضی شده بود، آن را از URL پاک می‌کنیم
                if "rt" in st.query_params:
                    del st.query_params["rt"]

    selected_page = render_sidebar()

    if selected_page == "🚀 ساخت پرامپت جدید":
        render_create_prompt_page()
    elif selected_page == "📚 تاریخچه پرامپت‌ها":
        render_history_page()
    elif selected_page == "📊 داشبورد کاربر":
        render_dashboard_page()

if __name__ == "__main__":
    main()
