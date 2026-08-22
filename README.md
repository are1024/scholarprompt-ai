# 🚀 ScholarPrompt AI

> **AI-Powered Academic Prompt Engineering Platform**  
> *Transform your research topics into precise, high-performance academic prompts for Large Language Models (LLMs).*

---

### 🌐 Language Selection / انتخاب زبان
You can read this documentation in:
* **[English Version](#-english-documentation)**
* **[نسخه فارسی (Farsi Documentation)](#-مستندات-فارسی)**

---

<a name="-english-documentation"></a>
# 🇬🇧 English Documentation

[![Streamlit App](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https:/scholarprompt-ai.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Supabase](https://img.shields.io/badge/Supabase-Database-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)](https://supabase.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

## 📖 Table of Contents
- [About the Project](#-about-the-project)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [Database Setup (Supabase)](#-database-setup-supabase)
- [Installation & Local Run](#-installation--local-run)
- [Deployment](#-deployment)

---

## 🎯 About the Project
**ScholarPrompt AI** is an advanced, specialized web application designed for researchers, graduate students, and academics. Writing effective prompts for Large Language Models (LLMs) requires deep understanding of prompt engineering. ScholarPrompt AI bridges this gap by automatically structuring user inputs into optimized, rigorous academic prompts.

## ✨ Key Features
- **Academic Parameter Structuring:** Tailors prompts based on Subject, Academic Level, Document Type, and Research Methodology.
- **Dual Access Control:** Guest users can generate prompts freely, while authenticated users can securely save and manage their prompt history.
- **Secure Cloud Database:** Integrated with Supabase for robust authentication and data persistence.

## 💻 Tech Stack
- **Frontend & Backend:** Python, Streamlit
- **Database & Auth:** Supabase (PostgreSQL)
- **Deployment:** Streamlit Cloud

## 🛠️ Database Setup (Supabase)
Run the following SQL query in your Supabase **SQL Editor**:
```sql
create table public.prompts (
id uuid default gen_random_uuid() primary key,
user_id uuid references auth.users(id) on delete cascade not null,
title text not null,
field text not null,
academic_level text not null,
document_type text not null,
methodology text not null,
generated_prompt text not null,
created_at timestamp with time zone default timezone('utc'::text, now()) not null
);
alter table public.prompts enable row level security;
create policy "Users can manage their own prompts" on public.prompts for all using (auth.uid() = user_id);

## ⚙️ Installation & Local Run
bash
git clone https://github.com/are1024/ScholarPrompt-AI.git
cd ScholarPrompt-AI
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py

---
---

<a name="-مستندات-فارسی"></a>
# 🇮🇷 مستندات فارسی (Farsi Documentation)

> **سامانه هوش مصنوعی مهندسی پرامپت آکادمیک**  
> *تبدیل موضوعات پژوهشی به پرامپت‌های دقیق و بهینه دانشگاهی برای مدل‌های زبانی بزرگ (LLMs).*

## 📖 فهرست مطالب
- [درباره پروژه](#-درباره-پروژه)
- [ویژگی‌های کلیدی](#-ویژگی‌های-کلیدی)
- [تکنولوژی‌های استفاده شده](#-تکنولوژی‌های-استفاده-شده)
- [راه‌اندازی پایگاه داده (Supabase)](#-راه‌اندازی-پایگاه-داده-supabase)
- [نصب و اجرای محلی](#-نصب-و-اجرای-محلی)
- [استقرار (Deployment)](#-استقرار-در-بستر-ابری)

---

## 🎯 درباره پروژه
سامانه **ScholarPrompt AI** یک وب‌اپلیکیشن پیشرفته است که به پژوهشگران، دانشجویان تحصیلات تکمیلی و اساتید کمک می‌کند تا پرامپت‌های استاندارد، علمی و ساختاریافته برای مدل‌های زبانی بزرگ (مانند GPT) تولید کنند. این سامانه با دریافت پارامترهای دقیق آکادمیک، بهترین نتیجه را برای نگارش پروپوزال، پایان‌نامه و مقالات فراهم می‌سازد.

## ✨ ویژگی‌های کلیدی
- **ساختاردهی پارامترهای آکادمیک:** تنظیم پرامپت بر اساس عنوان، رشته تحصیلی، مقطع (کارشناسی، ارشد، دکتری)، نوع سند و روش تحقیق (کمی، کیفی، آمیخته، مروری).
- **سطوح دسترسی دوگانه:** امکان تولید پرامپت برای کاربران مهمان (بدون نیاز به ثبت‌نام) و قابلیت ذخیره، مدیریت و بازیابی تاریخچه پرامپت‌ها برای کاربران ثبت‌نام‌شده.
- **پایگاه داده ابری امن:** اتصال کامل به `Supabase` جهت مدیریت احراز هویت و ذخیره‌سازی داده‌ها.

## 💻 تکنولوژی‌های استفاده شده
- **فرانت‌اند و بک‌اند:** پایتون (Python)، استریم‌لیت (Streamlit)
- **پایگاه داده و احراز هویت:** سوپابیس (Supabase / PostgreSQL)
- **کنترل نسخه و استقرار:** گیت‌هاب (GitHub)، استریم‌لیت کلود (Streamlit Cloud)

## 🛠️ راه‌اندازی پایگاه داده (Supabase)
برای ساخت جداول مورد نیاز، کد SQL زیر را در بخش **SQL Editor** در پنل Supabase اجرا کنید:
*(کد SQL در بخش انگلیسی بالا قابل کپی است)*

## ⚙️ نصب و اجرای محلی
برای اجرای پروژه روی سیستم شخصی خود، مراحل زیر را در ترمینال دنبال کنید:
bash
# ۱. کلون کردن مخزن
git clone https://github.com/are1024/ScholarPrompt-AI.git
cd ScholarPrompt-AI

# ۲. ایجاد محیط مجازی
python -m venv venv
source venv/bin/activate  # در ویندوز: venv\Scripts\activate

# ۳. نصب کتابخانه‌ها
pip install -r requirements.txt

# ۴. اجرای برنامه
streamlit run app.py

## ☁️ استقرار در بستر ابری
این پروژه روی پلتفرم **Streamlit Cloud** مستقر شده است. کافی است ریپازیتوری خود را به استریم‌لیت متصل کرده، متغیرهای محیطی پایگاه داده را در بخش Secrets وارد کنید و اپلیکیشن را به صورت **Public** دیپلوی نمایید.

---
<p align="center">Developed with ❤️ for Academic Excellence.</p>
