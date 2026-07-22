from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.prompt import AcademicPrompt

class IPromptRepository(ABC):
    
    @abstractmethod
    def save(self, prompt: AcademicPrompt) -> AcademicPrompt:
        """ذخیره یک پرامپت جدید در دیتابیس"""
        pass

    @abstractmethod
    def get_by_user_id(self, user_id: str) -> List[AcademicPrompt]:
        """دریافت لیست تمام پرامپت‌های یک کاربر"""
        pass

    @abstractmethod
    def delete_by_id(self, prompt_id: str, user_id: str) -> bool:
        """حذف یک پرامپت خاص"""
        pass
