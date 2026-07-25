import streamlit as st
from src.infrastructure.database.supabase_client import SupabaseManager

# پنجره پاپ‌آپ (Modal) برای ورود و ثبت‌نام
@st.dialog("حساب کاربری")
def auth_modal():
    supabase = SupabaseManager.get_client()
    
    tab_login, tab_signup = st.tabs(["ورود به حساب", "ثبت‌نام جدید"])
    
    with tab_login:
        with st.form("login_form"):
            email = st.text_input("ایمیل", key="login_email")
            password = st.text_input("رمز عبور", type="password", key="login_password")
            submit_login = st.form_submit_button("ورود")
            
            if submit_login:
                try:
                    response = supabase.auth.sign_in_with_password({"email": email, "password": password})
                    st.session_state.user = response.user
                    st.success("با موفقیت وارد شدید!")
                    st.rerun()
                except Exception as e:
                    st.error(f"خطا در ورود: {e}")
                    
    with tab_signup:
        with st.form("signup_form"):
            new_email = st.text_input("ایمیل", key="signup_email")
            new_password = st.text_input("رمز عبور (حداقل ۶ کاراکتر)", type="password", key="signup_password")
            submit_signup = st.form_submit_button("ثبت‌نام")
            
            if submit_signup:
                try:
                    response = supabase.auth.sign_up({"email": new_email, "password": new_password})
                    
                    # بررسی اینکه آیا ایمیل از قبل ثبت‌نام شده است یا خیر
                    if response and hasattr(response, 'user') and response.user and getattr(response.user, 'identities', None) == []:
                        st.error("این ایمیل قبلاً در سیستم ثبت‌نام شده است. لطفاً از بخش ورود استفاده کنید.")
                    else:
                        st.success("ثبت‌نام با موفقیت انجام شد! لطفاً ایمیل خود را برای تایید بررسی کنید.")
                        
                except Exception as e:
                    error_str = str(e)
                    if "already registered" in error_str.lower() or "user already registered" in error_str.lower():
                        st.error("این ایمیل قبلاً ثبت‌نام شده است. لطفاً به تب «ورود به حساب» مراجعه کنید.")
                    else:
                        st.error(f"خطا در ثبت‌نام: {error_str}")

def render_sidebar():
    with st.sidebar:
        st.image("https://img.icons8.com/isometric/100/graduation-cap.png", width=80)
        st.title("ScholarPrompt AI")
        st.caption("پلتفرم هوشمند تولید پرامپت‌های دانشگاهی")
        st.divider()

        selected_page = st.radio(
            "منوی اصلی",
            ["🚀 ساخت پرامپت جدید", "📚 تاریخچه پرامپت‌ها", "📊 داشبورد کاربر"],
            index=0
        )
        
        st.divider()
        
        # بخش مدیریت ورود و ثبت‌نام
        if "user" in st.session_state and st.session_state.user is not None:
            st.success(f"👤 خوش آمدید:\n{st.session_state.user.email}")
            if st.button("🚪 خروج از حساب", use_container_width=True):
                supabase = SupabaseManager.get_client()
                supabase.auth.sign_out()
                st.session_state.user = None
                st.rerun()
        else:
            if st.button("🔐 ورود / ثبت‌نام", use_container_width=True):
                auth_modal()
        
        return selected_page
