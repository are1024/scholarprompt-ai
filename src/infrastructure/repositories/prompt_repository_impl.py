from typing import List
from src.domain.entities.prompt import AcademicPrompt
from src.domain.repositories.prompt_repository import IPromptRepository
from src.infrastructure.database.supabase_client import SupabaseManager

class SupabasePromptRepository(IPromptRepository):
    
    def __init__(self):
        self.client = SupabaseManager.get_client()
        self.table_name = "prompts"

    def save(self, prompt: AcademicPrompt) -> AcademicPrompt:
        data = {
            "user_id": prompt.user_id,
            "title": prompt.title,
            "prompt_content": prompt.generated_prompt,
            "output_type": prompt.output_type,
            "language": prompt.language
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
            .eq("user_id", user_id)\
            .order("created_at", desc=True)\
            .execute()
            
        prompts = []
        for item in response.data:
            prompts.append(
                AcademicPrompt(
                    id=item.get("id"),
                    user_id=item.get("user_id"),
                    title=item.get("title"),
                    academic_field="نامشخص", # از محتوا خوانده می‌شود یا ثابت
                    degree="نامشخص",
                    output_type=item.get("output_type"),
                    generated_prompt=item.get("prompt_content"),
                    language=item.get("language", "fa"),
                    created_at=item.get("created_at")
                )
            )
        return prompts

    def delete_by_id(self, prompt_id: str, user_id: str) -> bool:
        response = self.client.table(self.table_name)\
            .delete()\
            .eq("id", prompt_id)\
            .eq("user_id", user_id)\
            .execute()
            
        return len(response.data) > 0
