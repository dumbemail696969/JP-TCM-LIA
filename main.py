from flask import Flask, render_template, request, jsonify
from openai import get_bot_response 
app = Flask(__name__)
@app.route('/')
def index():
    """Renders the main HTML template (templates/index.html)."""
    return render_template('index.html')
@app.route('/get_response', methods=['POST'])
def handle_message():
    try:
        user_message = request.json.get('message')
        if not user_message:
            return jsonify({'message': 'No message provided'}), 400
        bot_reply = get_bot_response(user_message)
        return jsonify({'message': bot_reply})
    except Exception as e:
        print(f"Application Error: {e}")
        return jsonify({'message': 'An internal server error occurred.'}), 500
if __name__ == '__main__':
    app.run(debug=True)
