from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv

# ✅ Load variables from .env
load_dotenv()

# ✅ Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# ✅ Flask app setup
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message sent"}), 400

    try:
        # ✅ Send message to OpenAI ChatGPT
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        reply = response.choices[0].message.content.strip()
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": f"❌ Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)

