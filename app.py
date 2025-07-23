from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "✅ Flask App is Running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.form  # Slack sends form-encoded data
    user_text = data.get('text', '')
    user_id = data.get('user_id', '')

    print("Received from Slack:", data)

    return jsonify({
        "response_type": "in_channel",
        "text": f"👋 Hi <@{user_id}>! You said: *{user_text}*"
    })
