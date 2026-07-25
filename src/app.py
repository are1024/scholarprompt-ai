
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
from src.infrastructure.database.supabase_client import SupabaseManager  # ایمپورت مدیریت سواس بیس

st.set_page_config(
    page_title="ScholarPrompt-AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"  # منو همیشه در ابتدا باز است
)


def main():
    apply_custom_css()

    # بررسی و حفظ وضعیت لاگین کاربر هنگام رفرش صفحه
    if "user" not in st.session_state:
        try:
            supabase = SupabaseManager.get_client()
            # تلاش برای گرفتن نشست فعال از طریق کوکی‌ها/حافظه سواس‌بییس
            session = supabase.auth.get_session()
            if session and session.user:
                st.session_state.user = session.user
        except Exception:
            pass  # اگر خطایی بود یعنی کاربر مهمان است و لاگین نکرده

    selected_page = render_sidebar()

    if selected_page == "🚀 ساخت پرامپت جدید":
        render_create_prompt_page()
    elif selected_page == "📚 تاریخچه پرامپت‌ها":
        render_history_page()
    elif selected_page == "📊 داشبورد کاربر":
        render_dashboard_page()

if __name__ == "__main__":
    main()
