from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class AcademicPrompt:
    id: Optional[str]
    user_id: str
    title: str
    academic_field: str       # رشته تحصیلی
    degree: str               # مقطع
    output_type: str          # پروپوزال، پایان‌نامه، مقاله، گزارش
    generated_prompt: str     # پرامپت نهایی ساخته‌شده
    language: str = "fa"
    created_at: Optional[datetime] = None
