import streamlit as st

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
        st.info("💡 **راهنما:** اطلاعات پژوهش خود را وارد کنید تا پرامپت ساختاریافته تولید شود.")
        
        return selected_page
