from flask import Flask, render_template, request, redirect, url_for, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pandas as pd
import os
from werkzeug.security import generate_password_hash, check_password_hash
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///phishing_sim.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)

db = SQLAlchemy(app)

# Custom filter for parsing JSON in templates
@app.template_filter('from_json')
def from_json(value):
    try:
        return json.loads(value)
    except:
        return {}

# Database Models
class PhishingEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    ip_address = db.Column(db.String(45), nullable=False)
    user_agent = db.Column(db.String(200), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    event_type = db.Column(db.String(20), nullable=False)  # 'click' or 'submit'
    submitted_data = db.Column(db.Text)  # JSON string of submitted form data

class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    template_id = db.Column(db.String(50), nullable=False)

# Routes
@app.route('/')
def index():
    return render_template('landing.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        'email': request.form.get('email'),
        'password': request.form.get('password'),
        'campaign_id': request.form.get('campaign_id')
    }
    
    event = PhishingEvent(
        campaign_id=data['campaign_id'],
        email=data['email'],
        ip_address=request.remote_addr,
        user_agent=request.user_agent.string,
        event_type='submit',
        submitted_data=json.dumps(data)
    )
    
    db.session.add(event)
    db.session.commit()
    
    return render_template('training.html')

@app.route('/track/<campaign_id>')
def track_click(campaign_id):
    event = PhishingEvent(
        campaign_id=campaign_id,
        email=request.args.get('email', 'unknown'),
        ip_address=request.remote_addr,
        user_agent=request.user_agent.string,
        event_type='click'
    )
    
    db.session.add(event)
    db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    events = PhishingEvent.query.order_by(PhishingEvent.timestamp.desc()).all()
    return render_template('dashboard.html', events=events)

@app.route('/export')
def export_data():
    events = PhishingEvent.query.all()
    data = []
    
    for event in events:
        data.append({
            'Campaign ID': event.campaign_id,
            'Email': event.email,
            'IP Address': event.ip_address,
            'User Agent': event.user_agent,
            'Timestamp': event.timestamp,
            'Event Type': event.event_type,
            'Submitted Data': event.submitted_data
        })
    
    df = pd.DataFrame(data)
    csv_path = 'phishing_report.csv'
    df.to_csv(csv_path, index=False)
    
    return send_file(csv_path, as_attachment=True)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True) 