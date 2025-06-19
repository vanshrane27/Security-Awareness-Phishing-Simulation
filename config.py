import os
from datetime import datetime, timedelta

# Database Configuration
DATABASE_PATH = 'phishing_sim.db'
SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE_PATH}'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Application Configuration
SECRET_KEY = os.urandom(24)
DEBUG = True

# Campaign Settings
DEFAULT_CAMPAIGN_DURATION = timedelta(days=7)
DEFAULT_CAMPAIGN_TEMPLATE = 'security_alert'

# Email Templates
EMAIL_TEMPLATES = {
    'security_alert': {
        'subject': 'Security Alert: Action Required',
        'body': '''
        Dear {user},

        We have detected unusual activity on your account. To ensure your account security, please verify your credentials immediately.

        Click here to verify: {link}

        If you did not request this verification, please contact support immediately.

        Best regards,
        Security Team
        '''
    },
    'password_reset': {
        'subject': 'Password Reset Request',
        'body': '''
        Dear {user},

        We received a request to reset your password. Click the link below to proceed:

        {link}

        If you did not request this password reset, please ignore this email.

        Best regards,
        Support Team
        '''
    }
}

# GoPhish Integration
GOPHISH_API_KEY = 'your_api_key_here'  # Replace with actual API key
GOPHISH_URL = 'http://localhost:3333'  # Replace with actual GoPhish URL

# Security Settings
ALLOWED_IPS = ['127.0.0.1']  # Add your internal IPs here
ADMIN_EMAILS = ['admin@example.com']  # Add admin emails here 