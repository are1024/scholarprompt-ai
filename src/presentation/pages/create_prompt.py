
import streamlit as st
import streamlit.components.v1 as components
from src.application.dto.prompt_dto import PromptCreateDTO
from src.application.services.prompt_service import PromptEngineService
from src.infrastructure.repositories.prompt_repository_impl import SupabasePromptRepository

def render_create_prompt_page():
    st.header("✨ ساخت پرامپت جدید")
    st.info("💡 **راهنما:** اطلاعات داخل فرم را تکمیل کنید و سپس روی دکمه تولید پرامپت هوشمند کلیک کنید تا پرامپت مدنظر تولید شود.")
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
            st.session_state.last_prompt_entity = prompt_entity
            
            # ریست کردن وضعیت ذخیره برای پرامپت جدید
            st.session_state.prompt_saved = False

        except Exception as e:
            st.error(f"خطایی رخ داد: {str(e)}")

    # ۴. نمایش پرامپت، دکمه کپی واقعی و دکمه ذخیره دستی
    if "last_generated_prompt" in st.session_state:
        st.success("پرامپت شما با موفقیت ساخته شد!")
        st.subheader("📋 پرامپت تولید شده:")
        
        prompt_text = st.session_state.last_generated_prompt
        st.code(prompt_text, language="markdown")

        # دکمه ذخیره دستی در تاریخچه با چک کردن تکراری نبودن
        if st.button("ذخیره پرامپت در تاریخچه 💾", use_container_width=True):
            user = st.session_state.get("user")
            if not user:
                st.error("⚠️ لطفاً ابتدا از منوی سمت راست وارد حساب کاربری خود شوید.")
            elif st.session_state.get("prompt_saved", False):
                st.warning("⚠️ این پرامپت قبلاً در تاریخچه ذخیره شده است!")
            else:
                try:
                    if "last_prompt_entity" in st.session_state:
                        repo = SupabasePromptRepository()
                        repo.save(st.session_state.last_prompt_entity)
                        st.session_state.prompt_saved = True  # علامت‌گذاری به عنوان ذخیره‌شده
                        st.success("✅ پرامپت با موفقیت در تاریخچه شما ذخیره شد!")
                    else:
                        st.warning("پرامپتی برای ذخیره یافت نشد.")
                except Exception as db_err:
                    st.error(f"خطا در ذخیره‌سازی: {str(db_err)}")

        # راهنمایی برای کاربران مهمان
        if not st.session_state.get("user"):
            st.info("💡 برای ذخیره این پرامپت در تاریخچه، لطفاً وارد حساب کاربری خود شوید.")