import os
import streamlit as st
from supabase import create_client, Client

class SupabaseManager:
    _client: Client = None

    @classmethod
    def get_client(cls) -> Client:
        if cls._client is None:
            # ۱. اول تلاش برای خواندن از Streamlit Secrets (محیط Cloud)
            url = st.secrets.get("SUPABASE_URL") if "SUPABASE_URL" in st.secrets else os.getenv("SUPABASE_URL")
            key = st.secrets.get("SUPABASE_KEY") if "SUPABASE_KEY" in st.secrets else os.getenv("SUPABASE_KEY")

            if not url or not key:
                raise ValueError("کلیدهای اتصالی Supabase یافت نشدند! لطفاً فایل env یا Secrets را بررسی کنید.")

            cls._client = create_client(url, key)
        return cls._client
