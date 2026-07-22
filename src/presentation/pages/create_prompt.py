import streamlit as st
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

            # ۲. فراخوانی سرویس تولید پرامپت
            # شناسه کاربر نمونه (در صورت نداشتن لاگین برای تست)
            dummy_user_id = st.session_state.get("user_id", "00000000-0000-0000-0000-000000000000")
            prompt_entity = PromptEngineService.generate_prompt(dto, user_id=dummy_user_id)

            # ۳. نمایش پرامپت تولید شده
            st.success("پرامپت شما با موفقیت بر اساس اصول Prompt Engineering ساخته شد!")
            st.subheader("📋 پرامپت تولید شده:")
            st.code(prompt_entity.generated_prompt, language="markdown")

            # ۴. تلاش برای ذخیره‌سازی در دیتابیس
            try:
                repo = SupabasePromptRepository()
                repo.save(prompt_entity)
                st.toast("پرامپت در تاریخچه شما ذخیره شد!", icon="✅")
            except Exception as db_err:
                st.warning(f"پرامپت ساخت شد اما در ذخیره‌سازی دیتابیس خطایی رخ داد: {db_err}")

        except Exception as e:
            st.error(f"خطایی رخ داد: {str(e)}")
