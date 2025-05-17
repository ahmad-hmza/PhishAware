import random
from datetime import datetime, timedelta
from email_templates import GENUINE_TEMPLATES, PHISHING_TEMPLATES

class EmailManager:
    def __init__(self):
        self.emails = []
        self.original_emails = []  # Store the original complete list
        
    def generate_emails(self):
        self.emails = []
        # Select random emails (more genuine than phishing for realism)
        selected_emails = random.sample(GENUINE_TEMPLATES, 10) + random.sample(PHISHING_TEMPLATES, 11)
        random.shuffle(selected_emails)
        
        for template in selected_emails:
            days_ago = random.randint(0, 9)
            date = (datetime.now() - timedelta(days=days_ago)).strftime("%Y-%m-%d %H:%M")
            
            email = {
                'from': template['sender'],
                'subject': template['subject'],
                'from_email': template['from_email'],
                'date': date,
                'body': template['body'],
                'link': template['link'],
                'attachments': template.get('attachments', []),
                'is_phishing': 'red_flags' in template,
                'red_flags': template.get('red_flags', []),
                'evaluated': False,
                'removed': False  # New flag to track removed emails
            }
            
            self.emails.append(email)
        
        self.original_emails = [email.copy() for email in self.emails]  # Save the original list
        return [email for email in self.emails if not email['removed']]
    
    def get_email(self, index):
        visible_emails = [email for email in self.emails if not email['removed']]
        if 0 <= index < len(visible_emails):
            return visible_emails[index]
        return None
    
    def remove_email(self, index):
        visible_emails = [email for email in self.emails if not email['removed']]
        if 0 <= index < len(visible_emails):
            email_to_remove = visible_emails[index]
            email_to_remove['removed'] = True
    
    def reset_emails(self):
        # Reset all emails to their original state
        self.emails = [email.copy() for email in self.original_emails]
        for email in self.emails:
            email['evaluated'] = False
            email['removed'] = False
        return self.emails

    def restore_removed_emails(self):
        for email in self.emails:
            email['removed'] = False  # Restore the removed flag
