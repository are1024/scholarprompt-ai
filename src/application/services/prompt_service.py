from src.application.dto.prompt_dto import PromptCreateDTO
from src.domain.entities.prompt import AcademicPrompt

class PromptEngineService:
    """موتور هوشمند تولید پرامپت‌های آکادمیک و دانشگاهی"""

    @staticmethod
    def generate_prompt(dto: PromptCreateDTO, user_id: str) -> AcademicPrompt:
        
        # ۱. الگوی استاندارد تعریف نقش و چارچوب اولیه
        system_role = (
            f"You are a Senior Academic Researcher and University Professor specializing in {dto.academic_field}.\n"
            f"Your expertise lies in supervising {dto.degree} level research, writing academic papers, thesis proposals, and research reports."
        )

        # ۲. تنظیم ساختار متناسب با نوع خروجی (پایان‌نامه، پروپوزال، مقاله و ...)
        output_structure = PromptEngineService._get_output_structure(dto.output_type)

        # ۳. سرجمع‌کردن و ساخت پرامپت نهایی (RTCC Pattern)
        constructed_prompt = f"""[SYSTEM ROLE & PERSONALITY]
{system_role}

[CONTEXT & RESEARCH SPECIFICATIONS]
- Research Title/Topic: {dto.title}
- Academic Level: {dto.degree}
- Discipline/Field: {dto.academic_field}
- Expected Output Type: {dto.output_type}
- Language: {dto.language}
{"- Methodology: " + dto.methodology if dto.methodology else ""}
{"- Special Instructions: " + dto.additional_notes if dto.additional_notes else ""}

[TASK INSTRUCTIONS]
Please generate a comprehensive, highly structured, and academic-grade {dto.output_type} draft for the topic above.
Follow the standard academic structure outlined below:

{output_structure}

[ACADEMIC CONSTRAINTS & QUALITY RULES]
1. Use a formal, objective, and scholarly tone (Academic Style).
2. Ensure rigorous logical structure between sections.
3. Include place-holders for proper citations (e.g., [Author, Year]) where references are required.
4. Avoid generic fluff; provide concrete, actionable, and deep research insights.
5. If writing in Persian, adhere to standard academic Persian literature style and punctuation rules.

Please proceed with generating the content accordingly.
"""

        # ۴. تبدیل خروجی به Entity دامنه
        return AcademicPrompt(
            id=None,
            user_id=user_id,
            title=dto.title,
            academic_field=dto.academic_field,
            degree=dto.degree,
            output_type=dto.output_type,
            generated_prompt=constructed_prompt,
            language=dto.language
        )

    @staticmethod
    def _get_output_structure(output_type: str) -> str:
        """ساختار استاندارد آکادمیک بر اساس نوع سند"""
        structures = {
            "پروپوزال": (
                "1. Title & Abstract\n"
                "2. Statement of the Problem (بیان مسئله)\n"
                "3. Research Questions & Hypotheses (سوالات و فرضیات)\n"
                "4. Significance & Innovation (ضرورت و نوآوری)\n"
                "5. Literature Review Summary (مروری بر ادبیات)\n"
                "6. Methodology & Data Collection (روش‌شناسی تحقیق)\n"
                "7. Expected Outcomes & Timeline (یافته‌های متوقع و زمان‌بندی)"
            ),
            "پایان‌نامه": (
                "1. Chapter 1: Introduction & Problem Statement\n"
                "2. Chapter 2: Literature Review & Theoretical Framework\n"
                "3. Chapter 3: Methodology & Research Design\n"
                "4. Chapter 4: Data Analysis & Results\n"
                "5. Chapter 5: Discussion, Conclusion & Future Work"
            ),
            "مقاله علمی": (
                "1. Abstract & Key Terms\n"
                "2. Introduction & Background\n"
                "3. Related Work\n"
                "4. Proposed Methodology\n"
                "5. Experiments / Case Study & Analysis\n"
                "6. Discussion & Limitations\n"
                "7. Conclusion & References Structure"
            ),
            "گزارش علمی": (
                "1. Executive Summary\n"
                "2. Introduction & Objectives\n"
                "3. Methodology / Technical Approach\n"
                "4. Main Findings & Discussion\n"
                "5. Practical Recommendations & Conclusion"
            )
        }
        return structures.get(output_type, "Standard Academic Outline: Introduction, Main Body, Methodology, Conclusion, References.")
