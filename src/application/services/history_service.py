from typing import List
from src.domain.entities.prompt import AcademicPrompt
from src.domain.repositories.prompt_repository import IPromptRepository

class HistoryService:
    
    def __init__(self, prompt_repo: IPromptRepository):
        self.prompt_repo = prompt_repo

    def get_user_history(self, user_id: str) -> List[AcademicPrompt]:
        """دریافت تاریخچه پرامپت‌های کاربر"""
        return self.prompt_repo.get_by_user_id(user_id)

    def delete_prompt(self, prompt_id: str, user_id: str) -> bool:
        """حذف پرامپت بر اساس شناسه"""
        return self.prompt_repo.delete_by_id(prompt_id, user_id)
