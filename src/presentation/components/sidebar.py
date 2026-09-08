import time
import streamlit as st

def render_sidebar():
    with st.sidebar:

        st.image(
            "https://img.icons8.com/isometric/100/graduation-cap.png",
            width=80
        )

        st.title("ScholarPrompt AI")
        st.caption("پلتفرم هوشمند تولید پرامپت‌های پژوهشی")
        st.divider()

        selected_page = st.radio(
            "منوی اصلی",
            [
                "🚀 ساخت پرامپت جدید",
                "📚 تاریخچه پرامپت‌ها",
                "📊 داشبورد کاربر"
            ],
            index=0
        )

        st.divider()

        # ورود و ثبت‌نام غیرفعال شده است
        if st.button("🔐 ورود / ثبت‌نام", use_container_width=True):
            st.info("ℹ️ ورود و ثبت‌نام در سایت لغو شده است.")

        # بخش شبکه‌های اجتماعی
        st.markdown("""
            <div style="text-align: center; margin-top: 20px;">
                <div style="display: flex; justify-content: center; gap: 20px; align-items: center;">
                    <!-- لینک یوتیوب -->
                    <a href="https://youtube.com" target="_blank" title="YouTube" style="color: #ff0000; text-decoration: none; display: flex; align-items: center;">
                        <svg height="22" width="22" viewBox="0 0 24 24" fill="currentColor">
                            <path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/>
                        </svg>
                    </a>
                    <!-- لینک تلگرام -->
                    <a href="https://t.me/scholarprompt_ai" target="_blank" title="Telegram" style="color: #0088cc; text-decoration: none; display: flex; align-items: center;">
                        <svg height="22" width="22" viewBox="0 0 24 24" fill="currentColor">
                            <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm5.562 8.161c-.18 1.897-.962 6.502-1.359 8.622-.168.9-.5 1.201-.82 1.23-.697.064-1.226-.461-1.901-.903-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.911.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635.099-.002.321.023.465.141.119.098.152.228.165.32-.016.12-.003.393-.112.59z"/>
                        </svg>
                    </a>
                    <!-- لینک گیت هاب -->
                    <a href="https://github.com/are1024/scholarprompt-ai" target="_blank" title="GitHub" style="color: inherit; text-decoration: none; display: flex; align-items: center;">
                        <svg height="20" width="20" viewBox="0 0 16 16" fill="currentColor">
                            <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.22 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path>
                        </svg>
                    </a>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        return selected_page
