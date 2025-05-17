import json
import os
from datetime import datetime

class UserManager:
    def __init__(self):
        self.score = 0
        self.total_emails = 0
        self.phishing_emails_reported = 0
        self.genuine_emails_reported = 0
        self.history = []
        self.user_name = ""
        
        # Create data directory if not exists
        if not os.path.exists("user_data"):
            os.makedirs("user_data")
    
    def set_user_name(self, name):
        self.user_name = name if name else "User"
    
    def record_action(self, action, email, was_correct):
        action_record = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "action": action,
            "email_subject": email['subject'],
            "sender": email['from'],
            "from_email": email['from_email'],
            "was_phishing": email['is_phishing'],
            "was_correct": was_correct,
            "score_impact": self.score
        }
    
    def update_score(self, is_phishing, correct):
        if correct:
            self.score += 20 if is_phishing else 10
            if is_phishing:
                self.phishing_emails_reported += 1
            else:
                self.genuine_emails_reported += 1
        else:
            self.score -= 15 if is_phishing else 10
    
    def save_history(self):
        try:
            with open("user_data/history.json", "w") as f:
                json.dump(self.history, f, indent=2)
        except Exception as e:
            print(f"Error saving history: {e}")
    
    def load_history(self):
        try:
            if os.path.exists("user_data/history.json"):
                with open("user_data/history.json", "r") as f:
                    self.history = json.load(f)
        except Exception as e:
            print(f"Error loading history: {e}")
    
    def add_session_to_history(self, total_emails):
        max_possible = total_emails * 20
        accuracy = (self.score / max_possible) * 100 if max_possible > 0 else 0
        
        session_data = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "score": self.score,
            "accuracy": accuracy,
            "phishing_caught": self.phishing_emails_reported,
            "genuine_correct": self.genuine_emails_reported,
            "total_emails": total_emails
        }
        self.history.append(session_data)
        self.save_history()