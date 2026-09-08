# 🚀 ScholarPrompt AI

> **AI-Powered Academic Prompt Engineering Platform**

**ScholarPrompt AI** is an AI-powered web application designed to help researchers, university students, and academics generate structured, precise, and high-quality prompts for Large Language Models (LLMs).

The platform transforms academic requirements into optimized prompts based on research field, academic level, document type, methodology, language, and additional requirements.

---

## 🌐 Language | زبان

* 🇬🇧 **English Documentation**
* 🇮🇷 **[مستندات فارسی](#-مستندات-فارسی)**

---

## 🔗 Live Demo

### 🎓 Try ScholarPrompt AI

**[Open the Web Application](https://scholarprompt-ai.streamlit.app/)**

The application is deployed using **Streamlit Community Cloud**.

> ⚠️ **Important Notice:** We apologize for the inconvenience. At this time, user login, registration, and Prompt storage features are unavailable in the system.

---

# 🇬🇧 English Documentation

## 📖 Overview

Creating effective prompts for Large Language Models requires more than simply asking a question. Academic tasks often require specific context, methodology, academic level, document type, language, and formatting requirements.

**ScholarPrompt AI** addresses this challenge by collecting structured academic information from the user and transforming it into a carefully designed academic prompt.

The generated prompt can then be used with Large Language Models such as ChatGPT, Claude, Gemini, and other compatible AI systems.

---

## 🎯 Project Goals

The main goals of ScholarPrompt AI are to:

* Simplify academic prompt engineering.
* Help users create structured and precise prompts.
* Reduce the difficulty of writing effective prompts for academic tasks.
* Provide prompts tailored to different academic levels and research methodologies.
* Allow authenticated users to save and manage their generated prompts.
* Provide a simple and accessible web-based interface.

---

## ✨ Key Features

### 🎓 Academic Parameter Structuring

The system generates prompts based on academic parameters such as:

* Research topic
* Academic field
* Academic degree
* Document type
* Research methodology
* Language
* Target AI model
* Additional requirements

### 🤖 AI-Powered Prompt Generation

ScholarPrompt AI transforms structured user requirements into optimized academic prompts suitable for Large Language Models.

### 👤 Guest Access

Users can generate academic prompts without creating an account.

### 🔐 Authentication & User Data

Authenticated users can securely store and manage their generated prompts.

### 📚 Prompt History

Registered users can:

* View previously generated prompts
* Retrieve their prompt history
* Delete unwanted prompts

### ☁️ Cloud Database

The application uses **Supabase PostgreSQL** for persistent data storage and Supabase Authentication for user management.

### 🖥️ Web-Based Interface

The user interface is implemented with **Streamlit**, providing a lightweight and interactive web experience.

---

## 🧠 How It Works

The general workflow of the application is:

```text
Academic Requirements
        ↓
User Input
        ↓
Data Validation
        ↓
Prompt Generation Engine
        ↓
Optimized Academic Prompt
        ↓
Display / Save
        ↓
User Prompt History
```

The system separates presentation, application logic, domain models, and infrastructure concerns according to Clean Architecture principles.

---

## 🏗️ Architecture

ScholarPrompt AI follows a **Clean Architecture** approach.

The architecture separates the system into different responsibilities:

### Presentation Layer

Responsible for the Streamlit user interface and interaction with users.

### Application Layer

Contains application services, DTOs, and the main application-level operations.

### Domain Layer

Contains the core business entities and repository abstractions.

### Infrastructure Layer

Responsible for external systems and implementations such as Supabase database connectivity and repository implementations.

This separation improves:

* Maintainability
* Scalability
* Testability
* Separation of concerns
* Future extensibility

---

## 🛠️ Tech Stack

| Technology                    | Purpose                                    |
| ----------------------------- | ------------------------------------------ |
| **Python**                    | Main programming language                  |
| **Streamlit**                 | Web interface and application framework    |
| **Supabase**                  | Database and authentication                |
| **PostgreSQL**                | Relational database                        |
| **Git**                       | Version control                            |
| **GitHub**                    | Source code management and project hosting |
| **Streamlit Community Cloud** | Application deployment                     |
| **Pydantic**                  | Data validation                            |
| **python-dotenv**             | Local environment configuration            |

---

## 🗄️ Database

ScholarPrompt AI uses **Supabase PostgreSQL** as its database.

The database stores information required for authenticated users and their generated prompts.

Database-related SQL scripts are maintained separately from this README.

### Database Schema

The SQL schema is available here:

**[📄 View Supabase Database Schema](supabase/schema.sql)**

### 🔐 Row Level Security

The application uses **Row Level Security (RLS)** to ensure that authenticated users can access only the records associated with their own accounts.

---

## ⚙️ Installation & Local Development

### Prerequisites

Before running the project locally, make sure the following are installed:

* Python 3.10 or newer
* Git
* A Supabase project

---

### 1. Clone the Repository

```bash
git clone https://github.com/are1024/ScholarPrompt-AI.git
cd ScholarPrompt-AI
```

---

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

---

### 3. Activate the Virtual Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Configure Environment Variables

Create a `.env` file in the project root.

Use the provided example as a reference:

```text
.env.example
```

Add the required Supabase configuration to your local `.env` file.

> **Important:** Never commit `.env` or any file containing API keys, passwords, or other sensitive credentials to GitHub.

---

### 6. Configure the Database

Open the SQL file:

**[supabase/schema.sql](supabase/schema.sql)**

Copy its contents into the **SQL Editor** of your Supabase project and execute the script.

---

### 7. Run the Application

Start the Streamlit application with:

```bash
streamlit run src/app.py
```

After running the command, Streamlit will provide a local URL where the application can be accessed.

---

## ☁️ Deployment

ScholarPrompt AI is deployed using **Streamlit Community Cloud**.

**Live Application:** [https://scholarprompt-ai.streamlit.app/](https://scholarprompt-ai.streamlit.app/)

> ⚠️ **Important Notice:** We apologize for the inconvenience. At this time, user login, registration, and Prompt storage features are unavailable in the system.

The general deployment process is:

1. Push the project to GitHub.
2. Connect the GitHub repository to Streamlit Community Cloud.
3. Select `src/app.py` as the application entry point.
4. Configure the required secrets.
5. Deploy the application.

The required Python dependencies are defined in:

```text
requirements.txt
```

Sensitive credentials should be configured through Streamlit's **Secrets** management rather than committed to the repository.

For more information, see the official Streamlit documentation:

**[Streamlit Community Cloud Documentation](https://docs.streamlit.io/deploy/streamlit-community-cloud)**

---

## 🔒 Security

Security-sensitive information is intentionally excluded from the repository.

The following files or information should **not** be committed:

```text
.env
API Keys
Passwords
Database Credentials
Private Tokens
```

The repository includes `.env.example` as a safe template for configuring the required environment variables.

---

## 📂 Database Configuration

Database configuration is intentionally separated from the main application documentation.

```text
supabase/schema.sql
```

This keeps the README concise while allowing developers to access the complete database setup script directly from the repository.

---

## 🧪 Development

The project is designed with separation of concerns in mind, allowing different parts of the application to be modified independently.

Future development can include:

* Additional academic document types
* More research methodologies
* Additional AI model integrations
* Advanced prompt templates
* Improved analytics
* Extended user management
* Additional language support

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

If you would like to contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Push the branch.
6. Open a Pull Request.

---

## 📜 License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for details.

---

# 🇮🇷 مستندات فارسی

## 🎯 معرفی پروژه

**ScholarPrompt AI** یک وب‌اپلیکیشن مبتنی بر هوش مصنوعی است که با هدف کمک به پژوهشگران، دانشجویان و دانشگاهیان برای تولید **پرامپت‌های دقیق، ساختاریافته و استاندارد دانشگاهی** طراحی شده است.

این سامانه اطلاعات آکادمیک مورد نیاز کاربر را دریافت کرده و بر اساس پارامترهایی مانند رشته تحصیلی، مقطع، نوع سند، روش تحقیق، زبان و سایر الزامات، یک پرامپت بهینه برای استفاده در مدل‌های زبانی بزرگ (LLMs) تولید می‌کند.

پرامپت تولیدشده می‌تواند در مدل‌هایی مانند ChatGPT، Claude، Gemini و سایر مدل‌های زبانی مورد استفاده قرار گیرد.

---

## 🎯 اهداف پروژه

اهداف اصلی ScholarPrompt AI عبارت‌اند از:

* ساده‌سازی فرآیند مهندسی پرامپت برای کارهای دانشگاهی
* کمک به تولید پرامپت‌های دقیق و ساختاریافته
* کاهش دشواری طراحی پرامپت برای فعالیت‌های پژوهشی
* تولید پرامپت متناسب با مقطع و حوزه دانشگاهی
* پشتیبانی از روش‌های مختلف تحقیق
* امکان ذخیره و مدیریت تاریخچه پرامپت‌ها برای کاربران ثبت‌نام‌شده
* ارائه یک رابط کاربری ساده و قابل دسترس

---

## ✨ ویژگی‌های کلیدی

### 🎓 ساختاردهی پارامترهای آکادمیک

تولید پرامپت بر اساس پارامترهایی مانند:

* موضوع پژوهش
* رشته تحصیلی
* مقطع تحصیلی
* نوع سند
* روش تحقیق
* زبان
* مدل هوش مصنوعی هدف
* توضیحات و الزامات اضافی

### 🤖 تولید پرامپت با کمک هوش مصنوعی

سامانه اطلاعات ساختاریافته کاربر را به یک پرامپت دقیق و بهینه برای مدل‌های زبانی بزرگ تبدیل می‌کند.

### 👤 دسترسی کاربران مهمان

کاربران می‌توانند بدون ثبت‌نام، پرامپت تولید کنند.

### 🔐 احراز هویت کاربران

کاربران ثبت‌نام‌شده می‌توانند پرامپت‌های خود را به صورت امن ذخیره و مدیریت کنند.

### 📚 تاریخچه پرامپت‌ها

کاربران ثبت‌نام‌شده می‌توانند:

* پرامپت‌های قبلی خود را مشاهده کنند
* تاریخچه پرامپت‌ها را بازیابی کنند
* پرامپت‌های موردنظر را حذف کنند

### ☁️ پایگاه داده ابری

برای ذخیره اطلاعات از **Supabase PostgreSQL** و برای مدیریت کاربران از **Supabase Authentication** استفاده شده است.

---

## 🧠 نحوه عملکرد سامانه

روند کلی عملکرد سیستم به شکل زیر است:

```text
نیاز پژوهشی
    ↓
ورودی کاربر
    ↓
اعتبارسنجی اطلاعات
    ↓
موتور تولید پرامپت
    ↓
پرامپت دانشگاهی بهینه‌شده
    ↓
نمایش / ذخیره‌سازی
    ↓
تاریخچه کاربر
```

---

## 🏗️ معماری سیستم

پروژه با رویکرد **Clean Architecture** طراحی شده است.

لایه‌های اصلی سیستم عبارت‌اند از:

* **Presentation:** رابط کاربری و تعامل با کاربر
* **Application:** سرویس‌ها و منطق سطح کاربرد
* **Domain:** موجودیت‌ها و انتزاعات اصلی سیستم
* **Infrastructure:** ارتباط با سرویس‌های خارجی و پایگاه داده

این تفکیک باعث بهبود:

* نگهداری کد
* توسعه‌پذیری
* تست‌پذیری
* جداسازی مسئولیت‌ها
* امکان توسعه قابلیت‌های آینده

می‌شود.

---

## 💻 فناوری‌های استفاده‌شده

| فناوری                        | کاربرد                     |
| ----------------------------- | -------------------------- |
| **Python**                    | زبان برنامه‌نویسی اصلی     |
| **Streamlit**                 | رابط کاربری و Framework وب |
| **Supabase**                  | پایگاه داده و احراز هویت   |
| **PostgreSQL**                | پایگاه داده رابطه‌ای       |
| **Git**                       | کنترل نسخه                 |
| **GitHub**                    | مدیریت و میزبانی کد        |
| **Streamlit Community Cloud** | استقرار برنامه             |
| **Pydantic**                  | اعتبارسنجی داده‌ها         |
| **python-dotenv**             | مدیریت تنظیمات محیط محلی   |

---

## 🗄️ پایگاه داده

پایگاه داده پروژه با استفاده از **Supabase PostgreSQL** پیاده‌سازی شده است.

کد SQL مربوط به ایجاد و تنظیم پایگاه داده در فایل زیر قرار دارد:

**[📄 مشاهده فایل SQL پایگاه داده](supabase/schema.sql)**

برای راه‌اندازی پایگاه داده کافی است محتوای این فایل را در بخش **SQL Editor** پروژه Supabase اجرا کنید.

### 🔐 امنیت پایگاه داده

برای جلوگیری از دسترسی کاربران به اطلاعات سایر کاربران، از قابلیت **Row Level Security (RLS)** استفاده شده است.

---

## ⚙️ نصب و اجرای محلی

### پیش‌نیازها

برای اجرای پروژه به موارد زیر نیاز دارید:

* Python 3.10 یا بالاتر
* Git
* یک پروژه در Supabase

### ۱. دریافت پروژه

```bash
git clone https://github.com/are1024/ScholarPrompt-AI.git
cd ScholarPrompt-AI
```

### ۲. ایجاد محیط مجازی

```bash
python -m venv .venv
```

### ۳. فعال‌سازی محیط مجازی

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### ۴. نصب وابستگی‌ها

```bash
pip install -r requirements.txt
```

### ۵. تنظیم متغیرهای محیطی

یک فایل `.env` در ریشه پروژه ایجاد کنید.

برای مشاهده نام متغیرهای موردنیاز می‌توانید از فایل زیر استفاده کنید:

```text
.env.example
```

> **توجه:** فایل `.env` و اطلاعات حساس مانند API Key، رمز عبور و اطلاعات اتصال پایگاه داده نباید در GitHub قرار گیرند.

### ۶. راه‌اندازی پایگاه داده

فایل زیر را باز کنید:

**[supabase/schema.sql](supabase/schema.sql)**

سپس محتوای آن را در **SQL Editor** پروژه Supabase اجرا کنید.

### ۷. اجرای برنامه

```bash
streamlit run src/app.py
```

پس از اجرای دستور، Streamlit یک آدرس محلی برای دسترسی به برنامه نمایش خواهد داد.

---

## ☁️ استقرار پروژه

پروژه **ScholarPrompt AI** با استفاده از **Streamlit Community Cloud** مستقر شده است.

**لینک اجرای آنلاین پروژه:** [https://scholarprompt-ai.streamlit.app/](https://scholarprompt-ai.streamlit.app/)

> ⚠️ **اطلاعیه مهم:** از بابت این موضوع پوزش می‌طلبیم. در حال حاضر قابلیت‌های ورود، ثبت‌نام کاربران و ذخیره‌سازی پرامپت در سامانه در دسترس نیستند.

مراحل کلی:

1. Push کردن پروژه در GitHub
2. اتصال Repository به Streamlit Community Cloud
3. انتخاب فایل `src/app.py` به عنوان Entry Point
4. تنظیم Secrets موردنیاز
5. Deploy کردن برنامه

وابستگی‌های پروژه در فایل زیر قرار دارند:

```text
requirements.txt
```

اطلاعات حساس باید از طریق بخش **Secrets** تنظیم شوند و نباید در Repository قرار بگیرند.

---

## 🔒 امنیت

اطلاعات حساس پروژه عمداً در Repository قرار داده نشده‌اند.

موارد زیر نباید در GitHub قرار گیرند:

```text
.env
API Keys
Passwords
Database Credentials
Private Tokens
```

فایل `.env.example` تنها برای نمایش ساختار متغیرهای محیطی موردنیاز پروژه استفاده می‌شود.

---

## 🤝 مشارکت

پیشنهادها، گزارش مشکلات و مشارکت در توسعه پروژه استقبال می‌شود.

برای مشارکت:

1. Repository را Fork کنید.
2. یک Branch جدید ایجاد کنید.
3. تغییرات موردنظر را اعمال کنید.
4. تغییرات را Commit کنید.
5. Branch را Push کنید.
6. یک Pull Request ایجاد کنید.

---

## 📜 مجوز

این پروژه تحت **MIT License** منتشر شده است.

برای اطلاعات بیشتر فایل [LICENSE](LICENSE) را مشاهده کنید.

---

<p align="center">
  <strong>Developed with ❤️ for Academic Excellence</strong>
</p>