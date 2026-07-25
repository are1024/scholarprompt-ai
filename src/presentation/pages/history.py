import streamlit as st
from src.infrastructure.repositories.prompt_repository_impl import SupabasePromptRepository
from src.application.services.history_service import HistoryService

def render_history_page():
    st.header("📚 تاریخچه پرامپت‌های ساخت‌شده")
    st.write("در این بخش می‌توانید پرامپت‌های قبلی خود را مشاهده، کپی یا مدیریت کنید.")

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

        for idx, prompt in enumerate(prompts):
            # نمایش عنوان (topic) و نوع سند (output_type)
            title = getattr(prompt, "title", "بدون عنوان")
            output_type = getattr(prompt, "output_type", "نامشخص")
            
            with st.expander(f"📌 {title} — ({output_type})", expanded=(idx == 0)):
                created_at = str(prompt.created_at) if prompt.created_at else 'نامشخص'
                date_str = created_at[:10] if created_at != 'نامشخص' else 'نامشخص'
                
                st.caption(f"📅 تاریخ ثبت: {date_str} | زبان: {prompt.language}")
                st.code(prompt.generated_prompt, language="markdown")
                
                col1, col2 = st.columns([1, 5])
                with col1:
                    if st.button("🗑️ حذف", key=f"del_{prompt.id}"):
                        if history_service.delete_prompt(prompt.id, user_id):
                            st.success("پرامپت با موفقیت حذف شد.")
                            st.rerun()

    except Exception as e:
        st.error(f"خطا در دریافت تاریخچه از دیتابیس: {str(e)}")
