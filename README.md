# Telegram Student Assistant Bot

This is a basic Telegram chatbot for student queries like marks, syllabus, and faculty availability using Flask and Python.

## 📦 Files
- `app.py` – main Flask application

## 🚀 Setup Instructions

1. Replace `"YOUR_TELEGRAM_BOT_TOKEN"` with your token from [@BotFather](https://t.me/BotFather)
2. Install requirements:
   ```
   pip install flask requests
   ```
3. Run the server:
   ```
   python app.py
   ```
4. Set the webhook:
   ```
   https://api.telegram.org/bot<YOUR_TOKEN>/setWebhook?url=<YOUR_PUBLIC_URL>
   ```

## 🔧 Customize
- Add more USNs and data to the `students` dictionary
- Extend functionality for dynamic data from Google Sheets or a database

