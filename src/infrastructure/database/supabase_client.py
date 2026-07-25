import os
from supabase import create_client, Client
from dotenv import load_dotenv
import streamlit as st

# بارگذاری متغیرها از فایل .env
load_dotenv()

class SupabaseManager:
    _client: Client = None

    @classmethod
    def get_client(cls) -> Client:
        if cls._client is None:
            url = None
            key = None
            
            # ۱. اول تلاش می‌کنیم از محیط لوکال (.env) بخوانیم
            url = os.getenv("SUPABASE_URL")
            key = os.getenv("SUPABASE_KEY")
            
            # ۲. اگر در لوکال نبود، برای دیپلوی روی استریم‌لیت کلود از st.secrets می‌خوانیم
            if not url or not key:
                try:
                    url = st.secrets.get("SUPABASE_URL")
                    key = st.secrets.get("SUPABASE_KEY")
                except Exception:
                    pass
            
            # ۳. اگر هیچ‌کدام تنظیم نشده بود، خطای واضح می‌دهیم
            if not url or not key:
                raise ValueError("تنظیمات Supabase (URL و Key) در فایل .env یا Streamlit Secrets یافت نشدند!")
                
            cls._client = create_client(url, key)
            
        return cls._client
