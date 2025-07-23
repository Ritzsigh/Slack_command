from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'GET':
        return "✅ Flask App is Running!"

    if request.method == 'POST':
        # Handle Slack slash command POST here
        user_id = request.form.get("user_id", "unknown user")
        command_text = request.form.get("text", "no text")

        print(f"Received POST from Slack: user={user_id}, text={command_text}")

        return jsonify({
            "response_type": "in_channel",
            "text": f"👋 Hello <@{user_id}>! You typed: *{command_text}*"
        })

if __name__ == '__main__':
    app.run(debug=True)
