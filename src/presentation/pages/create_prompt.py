import streamlit as st
import streamlit.components.v1 as components
from src.application.dto.prompt_dto import PromptCreateDTO
from src.application.services.prompt_service import PromptEngineService
from src.infrastructure.repositories.prompt_repository_impl import SupabasePromptRepository

def render_create_prompt_page():
    st.header("✨ ساخت پرامپت جدید")
    st.write("اطلاعات پژوهش خود را تکمیل کنید تا پرامپت استاندارد تولید شود.")

    with st.form("prompt_form"):
        col1, col2 = st.columns(2)

        with col1:
            title = st.text_input("عنوان یا موضوع پژوهش *", placeholder="مثلاً: بررسی اثر هوش مصنوعی بر یادگیری...")
            academic_field = st.text_input("رشته تحصیلی *", placeholder="مثلاً: مهندسی کامپیوتر")
            degree = st.selectbox("مقطع تحصیلی *", ["کارشناسی", "کارشناسی ارشد", "دکترا"])

        with col2:
            output_type = st.selectbox("نوع سند خروجی *", ["پروپوزال", "پایان‌نامه", "مقاله علمی", "گزارش علمی"])
            methodology = st.selectbox("روش تحقیق", ["کیفی (Qualitative)", "کمی (Quantitative)", "آمیخته (Mixed)", "مروری (Review)"])
            language = st.selectbox("زبان نگارش خروجی AI", ["فارسی (fa)", "انگلیسی (en)"])

        additional_notes = st.text_area("توضیحات یا محدودیت‌های خاص (اختیاری)", placeholder="مثلاً: تاکید روی متدولوژی x یا منابع سال ۲۰۲۰ به بعد...")

        submitted = st.form_submit_button("🔥 تولید پرامپت هوشمند", type="primary")

    if submitted:
        if not title or not academic_field:
            st.error("لطفاً موارد ستاره‌دار (عنوان و رشته تحصیلی) را وارد کنید.")
            return

        try:
            # ۱. ساخت DTO
            dto = PromptCreateDTO(
                title=title,
                academic_field=academic_field,
                degree=degree,
                output_type=output_type,
                language="fa" if language.startswith("فارسی") else "en",
                methodology=methodology,
                additional_notes=additional_notes
            )

            # بررسی وضعیت لاگین کاربر
            user = st.session_state.get("user")
            user_id = user.id if user else "00000000-0000-0000-0000-000000000000"

            # ۲. فراخوانی سرویس تولید پرامپت
            prompt_entity = PromptEngineService.generate_prompt(dto, user_id=user_id)

            # ذخیره در سشن
            st.session_state.last_generated_prompt = prompt_entity.generated_prompt

            # ۳. ذخیره‌سازی خودکار در دیتابیس (اگر کاربر لاگین باشد)
            if user:
                try:
                    repo = SupabasePromptRepository()
                    repo.save(prompt_entity)
                except Exception as db_err:
                    pass

        except Exception as e:
            st.error(f"خطایی رخ داد: {str(e)}")

    # ۴. نمایش پرامپت، دکمه کپی واقعی و پیام‌های وضعیت
    if "last_generated_prompt" in st.session_state:
        st.success("پرامپت شما با موفقیت ساخته شد!")
        st.subheader("📋 پرامپت تولید شده:")
        
        prompt_text = st.session_state.last_generated_prompt
        st.code(prompt_text, language="markdown")

        # ایمن‌سازی متن برای قرار گیری در کد جاوا اسکریپت
        text_to_copy = prompt_text.replace("\\", "\\\\").replace("`", "\\`").replace('"', '\\"').replace("\n", "\\n")

        # دکمه کپی اختصاصی با قابلیت کپی واقعی و نمایش Alert
        html_code = f"""
        <div style="display: flex; justify-content: center; margin-bottom: 15px;">
            <button onclick="copyToClipboard()" style="
                background-color: #2563eb;
                color: white;
                border: none;
                padding: 12px 20px;
                font-size: 16px;
                font-family: inherit;
                border-radius: 8px;
                cursor: pointer;
                width: 100%;
                font-weight: bold;
                box-shadow: 0 2px 5px rgba(0,0,0,0.2);
                transition: background 0.3s;
            ">📋 کپی کردن پرامپت</button>
        </div>
        <script>
        function copyToClipboard() {{
            navigator.clipboard.writeText(`{text_to_copy}`).then(function() {{
                alert("پرامپت کپی شد!");
            }}, function(err) {{
                alert("خطا در کپی کردن متن!");
            }});
        }}
        </script>
        """
        
        # نمایش دکمه کپی بالاتر از پیام‌های وضعیت
        components.html(html_code, height=65)

        # پیام وضعیت نهایی (ذخیره در تاریخچه یا درخواست لاگین)
        user = st.session_state.get("user")
        if user:
            st.toast("پرامپت در تاریخچه شما ذخیره شد!", icon="✅")
        else:
            st.info("💡 برای ذخیره خودکار این پرامپت در تاریخچه، لطفاً وارد حساب کاربری خود شوید.")
