from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class UserProfile:
    id: str
    email: str
    created_at: Optional[datetime] = None