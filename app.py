from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "✅ Flask App is Running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    user_id = request.form.get("user_id", "")
    user_text = request.form.get("text", "")

    print("From Slack:", request.form)

    return jsonify({
        "response_type": "in_channel",
        "text": f"👋 Hello <@{user_id}>! You said: *{user_text}*"
    })
