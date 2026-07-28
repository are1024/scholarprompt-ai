import streamlit as st
from src.infrastructure.repositories.prompt_repository_impl import SupabasePromptRepository
from src.infrastructure.database.supabase_client import SupabaseManager

# تعریف پنجره تأیید حذف حساب کاربری (Modal Dialog)
@st.dialog("⚠️ تأیید حذف دائمی حساب کاربری")
def delete_account_dialog(supabase):
    st.write("آیا از حذف حساب کاربری خود مطمئن هستید؟ این عمل غیرقابل بازگشت است.")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("بله، حذف شود", type="primary", use_container_width=True):
            try:
                # صدا زدن تابع امن دیتابیس برای حذف کاربر
                supabase.rpc('delete_user').execute()
                
                # خروج از سیستم و پاکسازی سشن
                supabase.auth.sign_out()
                st.session_state.clear()
                
                st.success("حساب کاربری و تمام پرامپت‌های شما با موفقیت حذف شدند.")
                st.rerun()
            except Exception as e:
                st.error(f"خطا در حذف حساب کاربری: {str(e)}")
    with col2:
        if st.button("خیر", use_container_width=True):
            st.rerun()

def render_dashboard_page():
    st.header("⚙️ تنظیمات حساب کاربری")
    
    # بررسی وضعیت لاگین واقعی کاربر از session_state
    user = st.session_state.get("user")
    
    if not user:
        st.warning("⚠️ لطفاً ابتدا برای دسترسی به تنظیمات، از طریق منوی کناری وارد حساب کاربری خود شوید.")
        return

    user_id = getattr(user, "id", None)
    if not user_id:
        st.error("خطا در شناسایی حساب کاربری. لطفاً دوباره وارد شوید.")
        return

    supabase = SupabaseManager.get_client()

    # استایل CSS برای قرمز کردن دکمه‌های Primary و مدیریت حالت غیرفعال (کم‌رنگ)
    st.markdown("""
        <style>
        div.stButton > button[kind="primary"] {
            background-color: #dc2626 !important;
            border-color: #dc2626 !important;
            color: white !important;
        }
        div.stButton > button[kind="primary"]:hover {
            background-color: #b91c1c !important;
            border-color: #b91c1c !important;
        }
        /* کم‌رنگ کردن دکمه پرایمری زمانی که disabled است */
        div.stButton > button[kind="primary"]:disabled {
            background-color: #dc2626 !important;
            border-color: #dc2626 !important;
            opacity: 0.4 !important;
            color: white !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # فرم تغییر اطلاعات حساب کاربری
    with st.form("update_account_form"):
        st.write(f"ایمیل فعلی: **{getattr(user, 'email', 'نامشخص')}**")
        
        new_email = st.text_input("ایمیل جدید (در صورت تمایل به تغییر)")
        new_password = st.text_input("رمز عبور جدید", type="password")
        confirm_password = st.text_input("تکرار رمز عبور جدید", type="password")
        
        submit_button = st.form_submit_button("بروزرسانی اطلاعات")
        
        if submit_button:
            update_data = {}
            
            if new_email:
                update_data["email"] = new_email
                
            if new_password or confirm_password:
                if new_password != confirm_password:
                    st.error("❌ رمز عبور جدید و تکرار آن با یکدیگر مطابقت ندارند.")
                elif len(new_password) < 6:
                    st.warning("⚠️ رمز عبور باید حداقل ۶ کاراکتر باشد.")
                else:
                    update_data["password"] = new_password

            if update_data:
                if "password" not in update_data or (new_password == confirm_password and len(new_password) >= 6):
                    try:
                        response = supabase.auth.update_user(update_data)
                        st.success("✅ اطلاعات حساب کاربری با موفقیت به‌روزرسانی شد.")
                        if new_email:
                            # نمایش پیام بررسی ایمیل به صورت Toast (شناور در گوشه صفحه)
                            st.toast("لطفاً ایمیل جدید خود را برای تایید بررسی کنید.", icon="⚠️")
                    except Exception as update_err:
                        st.error(f"خطا در به‌روزرسانی: {str(update_err)}")
            elif not new_email and not new_password:
                st.warning("لطفاً حداقل یکی از فیلدهای ایمیل یا رمز عبور را برای تغییر پر کنید.")

    st.divider()

    # بخش حذف حساب کاربری
    st.subheader("⚠️ حذف حساب کاربری")
    st.error("با حذف حساب کاربری، تمام اطلاعات و پرامپت‌های شما برای همیشه از دیتابیس پاک خواهند شد و این عمل غیرقابل بازگشت است.")
          
    confirm_delete = st.checkbox("‌ متوجه این اتفاق هستم و میخواهم حساب کاربری‌ام را حذف کنم.")

    
    if st.button("🗑️ حذف دائمی حساب کاربری", disabled=not confirm_delete, type="primary"):
        delete_account_dialog(supabase)
