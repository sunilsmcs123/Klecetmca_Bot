from flask import Flask, request
import requests

app = Flask(__name__)
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

# Dummy data
students = {
    "2KD23MC088": {
        "name": "Shruti",
        "marks": {"IA1": 18, "IA2": 20, "IA3": 22},
        "syllabus": {"DBMS": "5 out of 6 units completed"},
        "faculty": {"Ramesh": "In class till 12:00 PM"}
    }
}

@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    message = data['message']
    chat_id = message['chat']['id']
    text = message.get('text', '')

    if 'mark' in text.lower():
        reply = "Please enter your USN to get your marks."
    elif text.upper().startswith("2KD"):
        usn = text.strip().upper()
        info = students.get(usn)
        if info:
            m = info['marks']
            reply = f"Hi {info['name']}!\nYour IA Marks:\nIA1: {m['IA1']}\nIA2: {m['IA2']}\nIA3: {m['IA3']}"
        else:
            reply = "USN not found."
    elif 'syllabus' in text.lower():
        reply = students["2KD23MC088"]["syllabus"]["DBMS"]
    elif 'ramesh' in text.lower():
        reply = students["2KD23MC088"]["faculty"]["Ramesh"]
    else:
        reply = "Hello! Ask me about your marks, syllabus, or faculty availability."

    requests.post(TELEGRAM_URL, json={"chat_id": chat_id, "text": reply})
    return {"ok": True}
