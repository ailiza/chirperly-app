from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from .models import db, User, Contact, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://' #TODO
db.init_app(app)

@app.route('/')
def hello():
    return 'Hello from Chirperly Backend! :)'

@app.route('/get_response', methods=['POST'])
def get_response():
    data = request.get_json()
    message = data['message']
    conversation_history = data.get('conversation_history', [])

    suggested_responses = generate_responses(message, conversation_history)
    sentiment = analyze_sentiment(message)

    return jsonify({'responses': suggested_responses, 'sentiment': sentiment})

@app.route('/schedule_message', methods=['POST'])
def schedule_message():
    data = request.getjson()
    message = data['message']
    recipient = data['recipient']
    scheduled_time = data['scheduled_time'] #TODO: timing logic here

    #TODO: look into Celery or APScheduler
    schedule_message_task(message, recipient, scheduled_time)

    return jsonify({'status': 'success', 'message': 'Message_schedule'})

with app.app_context():
    db.create_all() 

if __name__ == '__main__':
    app.run(debug=True)