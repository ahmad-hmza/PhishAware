GENUINE_TEMPLATES = [
    {
        "sender": "IT Department",
        "subject": "Scheduled System Maintenance - March 15",
        "from_email": "it.support@yourcompany.com",
        "body": """Dear Team,

We would like to inform you about the scheduled system maintenance window:

Date: March 15, 2023
Time: 10:00 PM to 2:00 AM (EST)
Impact: All systems will be unavailable during this period

Please save your work and log out before the maintenance begins. 

For more details, visit our IT portal: https://it.yourcompany.com/maintenance

Thank you for your cooperation.

Best regards,
IT Support Team
yourcompany.com""",
        "link": "https://it.yourcompany.com/maintenance",
        "attachments": []
    },
    {
                "sender": "Human Resources",
                "subject": "Important: Benefits Enrollment Period Open",
                "from_email": "hr.benefits@yourcompany.com",
                "body": """Hello Colleagues,

The annual benefits enrollment period is now open from March 1-15. 

Please review your options and make your selections by the deadline. 

To access the enrollment system:
1. Visit https://hr.yourcompany.com/benefits
2. Log in with your employee credentials
3. Complete your enrollment

If you have questions, please contact benefits@yourcompany.com

Sincerely,
HR Benefits Team""",
                "link": "https://hr.yourcompany.com/benefits",
                "attachments": ["Benefits_Guide_2023.pdf"]
            },
            {
                "sender": "Security Team",
                "subject": "Reminder: Mandatory Security Training Due",
                "from_email": "security.training@yourcompany.com",
                "body": """Dear Employee,

This is a reminder that your annual security awareness training is due by March 31st.

To complete the training:
1. Log in to the Learning Portal: https://learn.yourcompany.com
2. Select "Security Awareness 2023"
3. Complete all modules and the final quiz

Note: Failure to complete this mandatory training may result in restricted system access.

For assistance, contact the Help Desk at ext. 4357.

Regards,
Corporate Security Team""",
                "link": "https://learn.yourcompany.com",
                "attachments": []
            },
            {
                "sender": "Payroll Department",
                "subject": "Your February 2023 Payslip is Available",
                "from_email": "payroll.notices@yourcompany.com",
                "body": """Dear Employee,

Your payslip for February 2023 is now available in the employee portal.

To access your payslip:
1. Go to https://portal.yourcompany.com
2. Log in with your credentials
3. Navigate to Payroll > Payslips

Please note: We will never email you a payslip directly for security reasons.

If you have any questions, please contact payroll@yourcompany.com

Sincerely,
Payroll Department""",
                "link": "https://portal.yourcompany.com",
                "attachments": []
            },
            {
                "sender": "Facilities Management",
                "subject": "Office Reopening Guidelines",
                "from_email": "facilities@yourcompany.com",
                "body": """Hello Everyone,

As we prepare for the full office reopening on April 3rd, please review the attached guidelines document.

Key points:
- New cleaning protocols
- Updated seating arrangements
- Conference room booking procedures

The full details are in the attached document.

Welcome back!

Facilities Team""",
                "link": "",
                "attachments": ["Office_Reopening_Guidelines.pdf"]
            },
            {
        "sender": "Amazon",
        "subject": "Your Order #123-4567890-1234567 Has Shipped",
        "from_email": "shipment-tracking@amazon.com",
        "body": """Hi,

Your Amazon order #123-4567890-1234567 has been shipped and is on the way.

Track your package: https://www.amazon.com/track/1234567

Thank you for shopping with us!
Amazon Team""",
        "link": "https://www.amazon.com/track/1234567",
        "attachments": []
            },
            {
        "sender": "PayPal",
        "subject": "Payment Confirmation - $65.00 to Netflix",
        "from_email": "service@paypal.com",
        "body": """Hello,

You’ve authorized a payment of $65.00 USD to Netflix.

Transaction ID: 4T12345678901234M
Date: May 10, 2025

View details: https://www.paypal.com/myaccount/transactions

Thanks,
PayPal""",
        "link": "https://www.paypal.com/myaccount/transactions",
        "attachments": []
            },
            {
    "sender": "Slack",
    "subject": "You have unread messages in #general",
    "from_email": "notifications@slack.com",
    "body": """Hi,

You have unread messages in the #general channel.

Catch up with your team: https://yourcompany.slack.com/messages/general

Thanks,
The Slack Team""",
    "link": "https://yourcompany.slack.com/messages/general",
    "attachments": []
            },
            {
    "sender": "Zoom",
    "subject": "Meeting Invitation: Project Sync",
    "from_email": "no-reply@zoom.us",
    "body": """You have been invited to the following Zoom meeting:

Topic: Weekly Project Sync
Time: May 15, 2025 10:00 AM

Join Zoom Meeting:
https://zoom.us/j/1234567890

Zoom Support""",
    "link": "https://zoom.us/j/1234567890",
    "attachments": []
            },
            {
    "sender": "Dropbox",
    "subject": "Shared File: Q2 Strategy Plan.pdf",
    "from_email": "no-reply@dropbox.com",
    "body": """Hi,

John has shared a file with you: Q2 Strategy Plan.pdf

View the file: https://www.dropbox.com/s/q2strategyplan

Dropbox""",
    "link": "https://www.dropbox.com/s/q2strategyplan",
    "attachments": []
            },
            {
    "sender": "Outlook Calendar",
    "subject": "Upcoming Event: Client Review Meeting",
    "from_email": "calendar-notify@outlook.com",
    "body": """This is a reminder for your upcoming event:

Event: Client Review Meeting
Date: May 17, 2025
Time: 2:00 PM

Join here: https://outlook.office365.com/meeting/abc123

Microsoft Outlook Calendar""",
    "link": "https://outlook.office365.com/meeting/abc123",
    "attachments": []
            },
            {
    "sender": "Indeed",
    "subject": "New Jobs Matching: Cybersecurity Analyst",
    "from_email": "alerts@indeed.com",
    "body": """Hi,

We found new job listings that match your search: "Cybersecurity Analyst".

View jobs: https://www.indeed.com/jobs?q=cybersecurity+analyst

Good luck!
Indeed""",
    "link": "https://www.indeed.com/jobs?q=cybersecurity+analyst",
    "attachments": []
            }
    
]

PHISHING_TEMPLATES = [
    {
        "sender": "IT Security",
        "subject": "URGENT: Unusual Login Activity Detected on Your Account",
        "from_email": "security-alert@your-company-support.com",
        "body": """URGENT SECURITY NOTIFICATION,

We detected unusual login activity on your account from a new device in Germany.

If this wasn't you, please secure your account immediately:

1. Click here to verify your identity: http://your-company-support.com/verify
2. Change your password
3. Review recent activity

Failure to respond within 24 hours will result in account suspension.

Security Team
Your Company Support""",
        "link": "http://your-company-support.com/verify",
        "attachments": [],
        "red_flags": [
            "Urgency created ('URGENT', '24 hours')",
            "Suspicious domain (your-company-support.com)",
            "Requests immediate action via link",
            "Generic greeting ('Your Account')",
            "Poor grammar and formatting"
        ]
    },
    {
                "sender": "Microsoft Office 365",
                "subject": "Your Subscription Will Be Suspended",
                "from_email": "noreply@office365-update.com",
                "body": """Dear Office 365 User,

Your subscription will be suspended due to a billing issue. To avoid service interruption:

1. Click here to update your payment details: http://office365-update.com/billing
2. Verify your account information

Important: You must complete this process within 12 hours to maintain access to your emails and files.

Microsoft Office 365 Team""",
                "link": "http://office365-update.com/billing",
                "attachments": ["Payment_Invoice_98342.pdf"],
                "red_flags": [
                    "Fake sender (not from microsoft.com)",
                    "Creates false urgency",
                    "Requests sensitive information",
                    "Attachment could be malicious",
                    "Unofficial domain (office365-update.com)"
                ]
            },
            {
                "sender": "LinkedIn Connections",
                "subject": "You have 3 new connection requests waiting",
                "from_email": "notifications@linkedin-mail.net",
                "body": """Hi there,

You have 3 new connection requests waiting for your response:

- John Smith (CEO at TechCorp)
- Sarah Johnson (Recruiter at TalentFinders)
- Michael Brown (HR Director at GlobalSoft)

View and respond to your pending requests:
http://linkedin-mail.net/connections

The LinkedIn Team""",
                "link": "http://linkedin-mail.net/connections",
                "attachments": [],
                "red_flags": [
                    "Fake LinkedIn domain (linkedin-mail.net)",
                    "Generic greeting ('Hi there')",
                    "Uses social engineering (important-sounding names)",
                    "Link goes to suspicious site"
                ]
            },
            {
                "sender": "DHL Express",
                "subject": "Package Delivery Failed - Action Required",
                "from_email": "delivery@dhl-express-tracking.com",
                "body": """Dear Customer,

We attempted to deliver your package today but were unsuccessful.

Tracking #: DHL78432905
Estimated Delivery Date: March 10, 2023
Recipient: Your Name

Please download and complete the attached delivery form and schedule a new delivery.

Download form: http://dhl-express-tracking.com/form

DHL Customer Service""",
                "link": "http://dhl-express-tracking.com/form",
                "attachments": ["Delivery_Form_DHL78432905.exe"],
                "red_flags": [
                    "Suspicious attachment (.exe file)",
                    "Fake DHL domain",
                    "Creates false urgency",
                    "Uses generic recipient ('Your Name')",
                    "Malicious executable attachment"
                ]
            },
            {
                "sender": "Your Bank",
                "subject": "Security Alert: Unusual Transaction Detected",
                "from_email": "alerts@your-bank-security.com",
                "body": """Dear Valued Customer,

We detected an unusual transaction attempt on your account:

Amount: $1,250.00
Merchant: Amazon Web Services
Location: Singapore

If you didn't authorize this transaction, please verify your account immediately:

http://your-bank-security.com/secure-login

For your security, we've temporarily restricted your account until verification is complete.

Bank Security Team""",
                "link": "http://your-bank-security.com/secure-login",
                "attachments": [],
                "red_flags": [
                    "Fake bank domain",
                    "Creates panic with false transaction",
                    "Requests login via link",
                    "Generic greeting ('Valued Customer')",
                    "Misspelled words"
                ]
            },
            {
                "sender": "Google Drive",
                "subject": "You've received a shared document",
                "from_email": "drive-share@google-docs.net",
                "body": """Hello,

You've received an important document shared via Google Drive:

Document: "Q1 Financial Report - Confidential"
Shared by: James Wilson (Finance Dept)

Click to view: http://google-docs.net/view/GFD7832

This link will expire in 24 hours.

Google Drive Team""",
                "link": "http://google-docs.net/view/GFD7832",
                "attachments": [],
                "red_flags": [
                    "Fake Google domain",
                    "Uses curiosity ('Confidential')",
                    "Creates false urgency ('expires in 24 hours')",
                    "Generic greeting",
                    "Link goes to suspicious site"
                ]
            },
            {
    "sender": "PayPal Support",
    "subject": "Your account is limited — action needed",
    "from_email": "alert@paypal-resolve.com",
    "body": """Dear User,

We've noticed unusual activity in your PayPal account.

To restore access, please verify your information:
http://paypal-resolve.com/login

PayPal Security""",
    "link": "http://paypal-resolve.com/login",
    "attachments": [],
    "red_flags": [
        "Fake PayPal domain",
        "Urgent action request",
        "Unsecured link"
    ]
            },
            {
    "sender": "Amazon Prime",
    "subject": "Your membership is expiring soon!",
    "from_email": "support@amazon-billing.com",
    "body": """Hello,

Your Amazon Prime subscription is expiring.

Renew here to continue benefits: http://amazon-billing.com/renew

Amazon Support""",
    "link": "http://amazon-billing.com/renew",
    "attachments": [],
    "red_flags": [
        "Fake billing domain",
        "Urgency",
        "Unsecured link"
    ]
            },
            {
    "sender": "Google Docs",
    "subject": "Shared confidential document: 'Budget2025'",
    "from_email": "drive@google-docs-services.com",
    "body": """Hi,

A confidential document has been shared with you.

View here: http://google-docs-services.com/shared/Budget2025

Google Drive""",
    "link": "http://google-docs-services.com/shared/Budget2025",
    "attachments": [],
    "red_flags": [
        "Fake domain",
        "Creates curiosity",
        "Unsecured external link"
    ]
            },
            {
    "sender": "Facebook Security",
    "subject": "Suspicious login attempt detected",
    "from_email": "secure@facebook-alerts.com",
    "body": """Hi,

We detected a suspicious login from Russia. If this wasn't you:

Secure your account now: http://facebook-alerts.com/security

Facebook""",
    "link": "http://facebook-alerts.com/security",
    "attachments": [],
    "red_flags": [
        "Scare tactic",
        "Impersonation of Facebook",
        "Look-alike domain"
    ]
            },
            {
    "sender": "Microsoft Support",
    "subject": "License Expired - Renew Now",
    "from_email": "admin@microsoft-renewal.com",
    "body": """Attention,

Your Microsoft Office license has expired.

Click below to renew:
http://microsoft-renewal.com/renew

Failure to act will disable access.

Microsoft""",
    "link": "http://microsoft-renewal.com/renew",
    "attachments": [],
    "red_flags": [
        "Fake renewal domain",
        "Fake urgency",
        "Unusual sender address"
    ]
            }
    
]