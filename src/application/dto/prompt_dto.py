from pydantic import BaseModel, Field
from typing import Optional

class PromptCreateDTO(BaseModel):
    title: str = Field(..., min_length=3, description="عنوان یا موضوع پژوهش")
    academic_field: str = Field(..., description="رشته تحصیلی")
    degree: str = Field(..., description="مقطع تحصیلی: کارشناسی، ارشد، دکترا")
    output_type: str = Field(..., description="نوع خروجی: پروپوزال، پایان‌نامه، مقاله، گزارش علمی")
    language: str = Field(default="fa", description="زبان نگارش پرامپت")
    methodology: Optional[str] = Field(default=None, description="روش تحقیق (کیفی، کمی، آمیخته)")
    target_ai: str = Field(default="ChatGPT / Claude", description="مدل هوش مصنوعی هدف")
    additional_notes: Optional[str] = Field(default=None, description="توضیحات یا محدودیت‌های خاص")
