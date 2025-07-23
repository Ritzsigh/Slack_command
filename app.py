from flask import Flask, request, jsonify

app = Flask(__name__)

# Root route for health check (GET and POST supported to avoid 405)
@app.route('/', methods=['GET', 'POST'])
def home():
    return "✅ Flask App is Running!"

# Webhook route for Slack to POST data
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("🔔 Received Slack data:", data)

    # Optionally process data here...

    return jsonify({
        "status": "success",
        "received": data
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
