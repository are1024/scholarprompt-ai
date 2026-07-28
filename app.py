import streamlit as st
from src.infrastructure.database.supabase_client import SupabaseManager
from src.presentation.components.sidebar import render_sidebar

# تنظیمات اولیه صفحه (باید اولین دستور استریم‌لیت باشد)
st.set_page_config(
    page_title="ScholarPrompt AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ۱. مقداردهی اولیه متغیرهای سشن برای ایزوله ماندن هر کاربر
if "user" not in st.session_state:
    st.session_state.user = None
if "access_token" not in st.session_state:
    st.session_state.access_token = None
if "refresh_token" not in st.session_state:
    st.session_state.refresh_token = None

# ۲. بازیابی نشست از طریق URL هنگام رفرش صفحه (F5)
supabase = SupabaseManager.get_client()

if "rt" in st.query_params and st.session_state.user is None:
    saved_rt = st.query_params["rt"]
    try:
        response = supabase.auth.set_session(refresh_token=saved_rt)
        if response and response.session:
            st.session_state.user = response.user
            st.session_state.access_token = response.session.access_token
            st.session_state.refresh_token = response.session.refresh_token
    except Exception as e:
        # اگر توکن منقضی یا نامعتبر بود، آن را از URL پاک می‌کنیم
        if "rt" in st.query_params:
            del st.query_params["rt"]

def main():
    # رندر کردن سایدبار و گرفتن صفحه انتخاب شده
    selected_page = render_sidebar()

    # مدیریت صفحات مختلف برنامه
    if selected_page == "🚀 ساخت پرامپت جدید":
        st.title("🚀 ساخت پرامپت دانشگاهی جدید")
        if st.session_state.user:
            st.info(f"شما با ایمیل ({st.session_state.user.email}) وارد شده‌اید.")
        else:
            st.warning("⚠️ برای دسترسی کامل به امکانات، لطفاً از طریق سایدبار وارد حساب خود شوید.")

    elif selected_page == "📚 تاریخچه پرامپت‌ها":
        st.title("📚 تاریخچه پرامپت‌های شما")
        if st.session_state.user:
            st.write("لیست پرامپت‌های ذخیره شده شما...")
        else:
            st.warning("لطفاً ابتدا وارد حساب کاربری خود شوید.")

    elif selected_page == "📊 داشبورد کاربر":
        st.title("📊 داشبورد مدیریت کاربر")
        if st.session_state.user:
            st.json({
                "Email": st.session_state.user.email,
                "User ID": st.session_state.user.id
            })
        else:
            st.warning("لطفاً ابتدا وارد حساب کاربری خود شوید.")

if __name__ == "__main__":
    main()
