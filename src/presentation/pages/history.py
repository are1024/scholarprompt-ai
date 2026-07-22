import streamlit as st
from src.infrastructure.repositories.prompt_repository_impl import SupabasePromptRepository
from src.application.services.history_service import HistoryService

def render_history_page():
    st.header("📚 تاریخچه پرامپت‌های ساخت‌شده")
    st.write("در این بخش می‌توانید پرامپت‌های قبلی خود را مشاهده، کپی یا مدیریت کنید.")

    dummy_user_id = st.session_state.get("user_id", "00000000-0000-0000-0000-000000000000")
    
    try:
        repo = SupabasePromptRepository()
        history_service = HistoryService(repo)
        prompts = history_service.get_user_history(dummy_user_id)

        if not prompts:
            st.info("هنوز هیچ پرامپتی ثبت نکرده‌اید. از منوی سمت راست یک پرامپت جدید بسازید!")
            return

        for idx, prompt in enumerate(prompts):
            with st.expander(f"📌 {prompt.title} — ({prompt.output_type})", expanded=(idx == 0)):
                st.caption(f"📅 تاریخ ثبت: {prompt.created_at[:10] if prompt.created_at else 'نامشخص'} | زبان: {prompt.language}")
                st.code(prompt.generated_prompt, language="markdown")
                
                col1, col2 = st.columns([1, 5])
                with col1:
                    if st.button("🗑️ حذف", key=f"del_{prompt.id}"):
                        if history_service.delete_prompt(prompt.id, dummy_user_id):
                            st.success("پرامپت با موفقیت حذف شد.")
                            st.rerun()

    except Exception as e:
        st.error(f"خطا در دریافت تاریخچه از دیتابیس: {str(e)}")
