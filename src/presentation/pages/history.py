import streamlit as st
from src.infrastructure.repositories.prompt_repository_impl import SupabasePromptRepository
from src.application.services.history_service import HistoryService

# تعریف پنجره تأیید حذف (Modal Dialog)
@st.dialog("⚠️ تأیید حذف پرامپت")
def delete_confirmation_dialog(prompt_id, user_id, history_service):
    st.write("آیا از حذف این پرامپت مطمئن هستید؟ این عملیات قابل بازگشت نیست.")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("بله، حذف شود", type="primary", use_container_width=True):
            if history_service.delete_prompt(prompt_id, user_id):
                st.success("پرامپت با موفقیت حذف شد.")
                st.rerun()
    with col2:
        if st.button("خیر", use_container_width=True):
            st.rerun()

def render_history_page():
    st.header("📚 تاریخچه پرامپت‌های ساخت‌شده")
    st.write("در این بخش می‌توانید پرامپت‌های قبلی خود را مشاهده و مدیریت کنید.")

    # بررسی وضعیت لاگین واقعی کاربر از session_state
    user = st.session_state.get("user")
    
    if not user:
        st.warning("⚠️ لطفاً ابتدا برای مشاهده تاریخچه، از طریق منوی کناری وارد حساب کاربری خود شوید.")
        return

    # دریافت شناسه کاربری واقعی (UUID) از شیء کاربر سپا بیس
    user_id = getattr(user, "id", None)
    if not user_id:
        st.error("خطا در شناسایی حساب کاربری. لطفاً دوباره وارد شوید.")
        return
    
    try:
        repo = SupabasePromptRepository()
        history_service = HistoryService(repo)
        prompts = history_service.get_user_history(user_id)

        if not prompts:
            st.info("هنوز هیچ پرامپتی ثبت نکرده‌اید. از صفحه ساخت پرامپت یک پرامپت جدید بسازید!")
            return

        # استایل برای قرمز کردن دکمه حذف (Primary)
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
            </style>
        """, unsafe_allow_html=True)

        for idx, prompt in enumerate(prompts):
            title = getattr(prompt, "title", "بدون عنوان")
            output_type = getattr(prompt, "output_type", "نامشخص")
            
            with st.expander(f"📌 {title} — ({output_type})", expanded=(idx == 0)):
                created_at = str(prompt.created_at) if prompt.created_at else 'نامشخص'
                date_str = created_at[:10] if created_at != 'نامشخص' else 'نامشخص'
                
                st.caption(f"📅 تاریخ ثبت: {date_str} | زبان: {prompt.language}")
                st.code(prompt.generated_prompt, language="markdown")
                
                # دکمه حذف که با کلیک روی آن پنجره تأیید باز می‌شود
                if st.button("🗑️ حذف پرامپت", key=f"del_{prompt.id}", type="primary", use_container_width=True):
                    delete_confirmation_dialog(prompt.id, user_id, history_service)

    except Exception as e:
        st.error(f"خطا در دریافت تاریخچه از دیتابیس: {str(e)}")
