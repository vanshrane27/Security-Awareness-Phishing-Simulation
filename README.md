# Security Awareness Phishing Simulation (SAPS)

A Flask-based application for conducting ethical phishing simulations and security awareness training.

## ⚠️ Important Notice

This tool is designed for **educational and training purposes only**. It should only be used:
- With explicit permission from all participants
- In controlled environments
- For security awareness training
- Never for actual phishing or malicious purposes

## 🚀 Features

- Simulated phishing landing pages
- Campaign tracking and analytics
- User click-through monitoring
- Detailed reporting dashboard
- CSV export functionality
- Integration with GoPhish for email campaigns

## 📋 Prerequisites

- Python 3.8+
- GoPhish (for email campaigns)
- SQLite3
- Virtual environment (recommended)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/SAPS.git
cd SAPS
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure GoPhish:
   - Install GoPhish following their [official documentation](https://docs.getgophish.com/user-guide/installation)
   - Update `config.py` with your GoPhish API key and URL

5. Initialize the database:
```bash
python
>>> from app import db
>>> db.create_all()
>>> exit()
```

## 🚀 Usage

1. Start the Flask application:
```bash
python app.py
```

2. Access the dashboard at `http://localhost:5000/dashboard`

3. Configure a campaign in GoPhish:
   - Create a new campaign
   - Use the provided email templates
   - Set the landing page URL to your Flask app's URL

4. Monitor results through the dashboard

## 📊 Dashboard Features

- View all campaign events
- Filter by date, IP, or email
- Export data to CSV
- Track click-through rates
- Monitor user submissions

## 🔒 Security Considerations

- All data is stored locally in SQLite
- No actual credentials are stored
- IP addresses and user agents are logged for training purposes
- Clear warning messages after form submission

## 📝 Configuration

Edit `config.py` to customize:
- Database settings
- Email templates
- Security settings
- GoPhish integration
- Allowed IPs and admin emails

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request


## ⚠️ Disclaimer

This tool is for educational purposes only. Users are responsible for ensuring they have proper authorization before conducting any phishing simulations. 


![Screenshot 2025-06-18 150523](https://github.com/user-attachments/assets/bdccfc3c-203d-4a16-a00d-facce1cd00e4)

![Screenshot 2025-06-18 150508](https://github.com/user-attachments/assets/18b93abe-35f3-4b29-8bde-0ca3d82fe18a)

![Screenshot 2025-06-19 084519](https://github.com/user-attachments/assets/2bfc5705-a273-4718-96b2-f318aacdfae7)

![Screenshot 2025-06-19 084730](https://github.com/user-attachments/assets/c6b4b7f4-f790-4b0b-952f-e1519d31b2d5)

![Screenshot 2025-06-19 084824](https://github.com/user-attachments/assets/343b7464-1fb9-4928-b6f4-174191aff140)
