from typing import List
from src.domain.entities.prompt import AcademicPrompt
from src.domain.repositories.prompt_repository import IPromptRepository
from src.infrastructure.database.supabase_client import SupabaseManager

class SupabasePromptRepository(IPromptRepository):
    
    def __init__(self):
        self.client = SupabaseManager.get_client()
        self.table_name = "prompts"

    def save(self, prompt: AcademicPrompt) -> AcademicPrompt:
        # نگاشت فیلدهای انتیتی به ستون‌های واقعی جدول شما در دیتابیس
        data = {
            "user_id": str(prompt.user_id),
            "topic": getattr(prompt, "topic", getattr(prompt, "title", "بدون عنوان")),
            "field_of_study": getattr(prompt, "field_of_study", getattr(prompt, "academic_field", "نامشخص")),
            "academic_level": getattr(prompt, "academic_level", getattr(prompt, "degree", "نامشخص")),
            "document_type": getattr(prompt, "document_type", getattr(prompt, "output_type", "نامشخص")),
            "language": getattr(prompt, "language", "fa"),
            "generated_prompt": prompt.generated_prompt
        }
        
        response = self.client.table(self.table_name).insert(data).execute()
        
        if response.data:
            inserted_item = response.data[0]
            prompt.id = inserted_item.get("id")
            prompt.created_at = inserted_item.get("created_at")
            return prompt
        
        raise Exception("خطا در ذخیره‌سازی پرامپت در پایگاه داده")

    def get_by_user_id(self, user_id: str) -> List[AcademicPrompt]:
        response = self.client.table(self.table_name)\
            .select("*")\
            .eq("user_id", str(user_id))\
            .order("created_at", desc=True)\
            .execute()
            
        prompts = []
        for item in response.data:
            prompts.append(
                AcademicPrompt(
                    id=item.get("id"),
                    user_id=item.get("user_id"),
                    # خواندن از ستون‌های دیتابیس شما و پر کردن انتیتی
                    title=item.get("topic"), 
                    academic_field=item.get("field_of_study"),
                    degree=item.get("academic_level"),
                    output_type=item.get("document_type"),
                    generated_prompt=item.get("generated_prompt"),
                    language=item.get("language", "fa"),
                    created_at=item.get("created_at")
                )
            )
        return prompts

    def delete_by_id(self, prompt_id: str, user_id: str) -> bool:
        response = self.client.table(self.table_name)\
            .delete()\
            .eq("id", prompt_id)\
            .eq("user_id", str(user_id))\
            .execute()
            
        return len(response.data) > 0
