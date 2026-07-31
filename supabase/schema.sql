-- ۱. ساخت جدول پرامپت‌ها و تنظیمات امنیتی آن
CREATE TABLE IF NOT EXISTS public.prompts (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
    topic TEXT NOT NULL,
    field_of_study TEXT NOT NULL,
    academic_level TEXT NOT NULL,
    document_type TEXT NOT NULL,
    language TEXT DEFAULT 'fa',
    generated_prompt TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

ALTER TABLE public.prompts ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS "Users can manage their own prompts" ON public.prompts;

CREATE POLICY "Users can manage their own prompts" 
ON public.prompts 
FOR ALL 
USING (auth.uid() = user_id)
WITH CHECK (auth.uid() = user_id);


-- ۲. تابع حذف حساب کاربری (فقط برای کاربران لاگین‌شده)
create or replace function delete_user()
returns void
language plpgsql
security definer
as $$
begin
  delete from auth.users where id = auth.uid();
end;
$$;

grant execute on function public.delete_user() to authenticated;