import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

class SupabaseManager:
    _instance: Client = None

    @classmethod
    def get_client(cls) -> Client:
        if cls._instance is None:
            url: str = os.getenv("SUPABASE_URL", "")
            key: str = os.getenv("SUPABASE_KEY", "")
            
            if not url or not key:
                raise ValueError("SUPABASE_URL and SUPABASE_KEY must be set in .env file")
                
            cls._instance = create_client(url, key)
        return cls._instance
