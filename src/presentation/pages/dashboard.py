import streamlit as st
from src.infrastructure.repositories.prompt_repository_impl import SupabasePromptRepository

def render_dashboard_page():
    st.header("📊 داشبورد آماری پژوهشگر")
    
    dummy_user_id = st.session_state.get("user_id", "00000000-0000-0000-0000-000000000000")

    try:
        repo = SupabasePromptRepository()
        prompts = repo.get_by_user_id(dummy_user_id)
        
        col1, col2, col3 = st.columns(3)
        col1.metric("تعداد کل پرامپت‌ها", len(prompts))
        
        proposals_count = sum(1 for p in prompts if p.output_type == "پروپوزال")
        col2.metric("پروپوزال‌های تولید شده", proposals_count)
        
        theses_count = sum(1 for p in prompts if p.output_type == "پایان‌نامه")
        col3.metric("بخش‌های پایان‌نامه", theses_count)

        st.divider()
        st.subheader("💡 راهنمای استفاده بهینه")
        st.markdown("""
        - **پروپوزال:** برای ساخت بیان مسئله و اهمیت تحقیق استفاده کنید.
        - **پایان‌نامه:** برای تدوین فصل‌بندی و چارچوب نظری مناسب است.
        - **مقاله:** برای نوشتن چکیده و ساختار مقاله ISI توصیه می‌شود.
        """)
    except Exception as e:
        st.error(f"خطا در دریافت آمار: {str(e)}")
