# PhishAware

## Overview

The Phishing Simulator is an educational tool designed to help users recognize and respond to phishing attacks. By simulating various phishing scenarios, this project aims to raise awareness about the tactics used by cybercriminals and improve users' ability to identify suspicious emails. The simulator generates both genuine and phishing emails, allowing users to practice their skills in a safe environment.

## Features

- **Email Generation**: Randomly generates a mix of genuine and phishing emails to simulate real-world scenarios.
- **Phishing Detection**: Users can evaluate emails and report them as phishing or genuine, enhancing their ability to identify threats.
- **Email Details**: Displays detailed information about each email, including sender, subject, body, and any attachments.
- **Score Tracking**: Keeps track of user performance, including the number of phishing emails correctly identified and genuine emails reported.
- **Tutorial**: Provides educational content on phishing awareness, including common red flags and best practices for avoiding phishing attacks.

## Problem Statement

Phishing attacks are one of the most common and effective methods used by cybercriminals to steal sensitive information. Many users lack the knowledge and skills to identify phishing attempts, leading to compromised accounts and data breaches. This simulator addresses the need for practical training in recognizing phishing emails and understanding the associated risks.

## Design

The Phishing Simulator is built using Python and leverages the following components:

- **Email Manager**: Responsible for generating and managing the list of emails, including both genuine and phishing templates.
- **User  Interface**: A graphical user interface (GUI) built with PyQt that allows users to interact with the simulator, view emails, and report phishing attempts.
- **Tutorial Module**: Provides users with educational content on phishing, including how to spot phishing emails and best practices for online safety.

## Workflow

The simulator follows a structured workflow to ensure an engaging and educational experience for users:

1. **User  Onboarding**: Users are prompted to enter their name and start a new session.
2. **Email Generation**: The simulator generates a set of emails, mixing genuine and phishing attempts.
3. **Email Evaluation**: Users can select an email to view its details and decide whether to report it as phishing or genuine.
4. **Score Update**: The simulator updates the user's score based on their evaluations, providing feedback on their performance.
5. **Tutorial Access**: Users can access a tutorial at any time to learn more about phishing and improve their skills.
6. **Session Summary**: At the end of the session, users receive a summary of their performance, including the number of phishing emails identified and their overall score.

## Implementation

The project is implemented in Python and utilizes the following libraries:

- **PyQt**: For building the graphical user interface.
- **Random**: For generating random emails from predefined templates.
- **Datetime**: For managing email timestamps.

### Code Snippet

Here’s a brief code snippet illustrating the email generation process:

```python
import random
from datetime import datetime, timedelta

class EmailManager:
    def generate_emails(self):
        # Logic to generate emails
        pass
