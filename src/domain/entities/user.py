from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class UserProfile:
    id: str
    email: str
    full_name: str
    degree: Optional[str] = None      # مقطع تحصیلی
    university: Optional[str] = None  # دانشگاه
    created_at: Optional[datetime] = None
