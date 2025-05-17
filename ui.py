import sys
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QPushButton, QListWidget, QTextEdit, QMenu, QMenuBar, 
                             QMessageBox, QInputDialog, QDialog, QScrollArea, QTabWidget, 
                             QSplitter, QFrame, QProgressBar, QListWidgetItem, QGridLayout)
from PyQt6.QtCore import Qt, QSize, QEvent
from PyQt6.QtGui import QFont, QIcon, QAction, QColor, QPalette, QPixmap, QImage
from email_manager import EmailManager
from user_manager import UserManager
from tutorial import get_tutorial_content

class EmailListItem(QListWidgetItem):
    def __init__(self, email):
        display_text = f"{email['from']} - {email['subject']}"
        if email['attachments']:
            display_text += " 📎"
        
        super().__init__(display_text)
        self.email = email
        
        # Style based on whether it's read or not
        self.setFont(QFont("Segoe UI", 10))
        
        # Add metadata
        self.setData(Qt.ItemDataRole.UserRole, email)

class TutorialDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Phishing Awareness Tutorial")
        self.setMinimumSize(700, 500)
        
        layout = QVBoxLayout()
        
        # Create tab widget for tutorial sections
        tabs = QTabWidget()
        tutorial_content = get_tutorial_content()
        
        for title, content in tutorial_content.items():
            tab = QWidget()
            tab_layout = QVBoxLayout()
            
            text_display = QTextEdit()
            text_display.setReadOnly(True)
            text_display.setHtml(self._format_content(content))
            
            tab_layout.addWidget(text_display)
            tab.setLayout(tab_layout)
            tabs.addTab(tab, title)
        
        layout.addWidget(tabs)
        
        # Add close button
        close_button = QPushButton("Got it!")
        close_button.clicked.connect(self.accept)
        
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(close_button)
        button_layout.addStretch()
        
        layout.addLayout(button_layout)
        self.setLayout(layout)
    
    def _format_content(self, content):
        # Convert plain text to HTML with better formatting
        html_content = content.replace('\n', '<br>')
        
        # Format bullet points
        html_content = html_content.replace('• ', '<br>• ')
        
        # Format section titles
        lines = html_content.split('<br>')
        formatted_lines = []
        
        for line in lines:
            if ':' in line and len(line.split(':')[0]) < 40:  # Likely a section title
                parts = line.split(':')
                title = parts[0]
                rest = ':'.join(parts[1:])
                formatted_lines.append(f"<h3>{title}:</h3>{rest}")
            else:
                formatted_lines.append(line)
        
        html_content = '<br>'.join(formatted_lines)
        
        # Add general styling - updated for dark mode
        html_content = f"""
        <style>
            body {{
                background-color: #232323;
                color: #FFFFFF;
                padding: 10px;
            }}
            h3 {{
                color: #4a86e8;
                font-size: 18px;
                margin-top: 20px;
                margin-bottom: 10px;
                border-bottom: 1px solid #444444;
                padding-bottom: 5px;
            }}
            ul {{
                margin-left: 20px;
            }}
            • {{
                margin-bottom: 8px;
                color: #EEEEEE;
            }}
            p {{
                color: #EEEEEE;
                margin: 8px 0;
            }}
        </style>
        <div style="font-family: 'Segoe UI', Arial, sans-serif; line-height: 1.6; color: #EEEEEE; background-color: #232323; padding: 15px; border-radius: 5px;">
            {html_content}
        </div>
        """
        
        return html_content

class EmailSimulator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.email_manager = EmailManager()
        self.user_manager = UserManager()
        self.tutorial_shown = False
        
        self.setWindowTitle("Advanced Phishing Awareness Simulator")
        self.setMinimumSize(1000, 700)
        
        # Set application icon if available
        icon_path = "icon.png"  # Use the icon.png file
        if os.path.exists(icon_path):
            # Load the icon as QImage
            image = QImage(icon_path)
            # Invert the colors
            image.invertPixels()
            
            # Convert back to pixmap and create icon
            pixmap = QPixmap.fromImage(image)
            icon = QIcon(pixmap)
            self.setWindowIcon(icon)
        
        self.init_ui()
        self.show_welcome()
    
    def init_ui(self):
        # Create central widget
        central_widget = QWidget()
        main_layout = QVBoxLayout()
        
        # Header with logo and title
        header_frame = QFrame()
        header_frame.setMaximumHeight(80)
        header_layout = QHBoxLayout(header_frame)
        header_layout.setContentsMargins(20, 10, 20, 10)
        
        # Create logo if it exists (or use text)
        logo_label = QLabel("🛡️")  # Email shield emoji as placeholder
        logo_label.setFont(QFont("Segoe UI", 32))
        logo_label.setStyleSheet("color: #4a86e8;")
        header_layout.addWidget(logo_label)
        
        title_label = QLabel("Advanced Phishing Awareness Simulator")
        title_label.setFont(QFont("Segoe UI", 24, QFont.Weight.Bold))
        title_label.setStyleSheet("color: #4a86e8;")
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        
        main_layout.addWidget(header_frame)
        
        # Add a horizontal line separator
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setFrameShadow(QFrame.Shadow.Sunken)
        separator.setStyleSheet("background-color: #444444; max-height: 1px; margin: 0 20px;")
        main_layout.addWidget(separator)
        
        # User info and score section
        info_frame = QFrame()
        info_frame.setMaximumHeight(100)
        info_layout = QHBoxLayout(info_frame)
        info_layout.setContentsMargins(20, 10, 20, 10)
        
        # User info
        user_frame = QFrame()
        user_layout = QVBoxLayout(user_frame)
        self.user_label = QLabel("User: Guest")
        self.user_label.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))
        self.user_label.setStyleSheet("color: #FFFFFF;")
        user_layout.addWidget(self.user_label)
        info_layout.addWidget(user_frame)
        
        info_layout.addStretch()
        
        # Score display
        score_frame = QFrame()
        score_layout = QVBoxLayout(score_frame)
        self.score_label = QLabel(f"Score: {self.user_manager.score}")
        self.score_label.setFont(QFont("Segoe UI", 18, QFont.Weight.Bold))
        self.score_label.setStyleSheet("color: #2ecc71;")
        self.score_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        score_layout.addWidget(self.score_label)
        
        # Progress bar for score visualization
        self.score_progress = QProgressBar()
        self.score_progress.setRange(0, 200)  # Assuming max score around 200
        self.score_progress.setValue(0)
        self.score_progress.setTextVisible(False)
        self.score_progress.setMinimumWidth(200)
        self.score_progress.setMaximumHeight(10)
        score_layout.addWidget(self.score_progress)
        
        info_layout.addWidget(score_frame)
        info_layout.addStretch()
        
        # Stats display
        stats_frame = QFrame()
        stats_layout = QVBoxLayout(stats_frame)
        self.stats_label = QLabel("Phishing Reported: 0 | Genuine Reported: 0")
        self.stats_label.setFont(QFont("Segoe UI", 12))
        self.stats_label.setStyleSheet("color: #CCCCCC;")
        stats_layout.addWidget(self.stats_label)
        info_layout.addWidget(stats_frame)
        
        main_layout.addWidget(info_frame)
        
        # Create content area with drop shadow effect
        content_frame = QFrame()
        content_frame.setStyleSheet("background-color: #232323; border-radius: 8px;")
        content_layout = QVBoxLayout(content_frame)
        
        # Create splitter for email list and details
        splitter = QSplitter(Qt.Orientation.Vertical)
        splitter.setHandleWidth(2)
        splitter.setStyleSheet("QSplitter::handle { background-color: #444444; }")
        
        # Email list section
        list_widget = QWidget()
        list_widget.setStyleSheet("background-color: transparent;")
        list_layout = QVBoxLayout(list_widget)
        list_layout.setContentsMargins(15, 15, 15, 15)
        
        list_header = QLabel("Your Inbox")
        list_header.setFont(QFont("Segoe UI", 16, QFont.Weight.Bold))
        list_header.setStyleSheet("color: #4a86e8;")
        list_layout.addWidget(list_header)
        
        self.email_list = QListWidget()
        self.email_list.setFont(QFont("Segoe UI", 12))
        self.email_list.setStyleSheet("""
            QListWidget {
                background-color: #2A2A2A;
                border-radius: 5px;
                padding: 5px;
            }
        """)
        self.email_list.currentItemChanged.connect(self.show_email_details)
        self.email_list.itemDoubleClicked.connect(self.open_email_link)
        list_layout.addWidget(self.email_list)
        
        # Email details section
        details_widget = QWidget()
        details_widget.setStyleSheet("background-color: transparent;")
        details_layout = QVBoxLayout(details_widget)
        details_layout.setContentsMargins(15, 15, 15, 15)
        
        details_header = QLabel("Email Content")
        details_header.setFont(QFont("Segoe UI", 16, QFont.Weight.Bold))
        details_header.setStyleSheet("color: #4a86e8;")
        details_layout.addWidget(details_header)
        
        self.details_text = QTextEdit()
        self.details_text.setReadOnly(True)
        self.details_text.setStyleSheet("""
            QTextEdit {
                background-color: #2A2A2A;
                border-radius: 5px;
                padding: 5px;
                font-family: 'Segoe UI', sans-serif;
                font-size: 13px;
            }
        """)
        details_layout.addWidget(self.details_text)
        
        # Attachment section
        attachment_layout = QHBoxLayout()
        attachment_header = QLabel("Attachments:")
        attachment_header.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        attachment_header.setStyleSheet("color: #CCCCCC;")
        attachment_layout.addWidget(attachment_header)
        
        self.attachment_container = QHBoxLayout()
        attachment_layout.addLayout(self.attachment_container)
        attachment_layout.addStretch()
        details_layout.addLayout(attachment_layout)
        
        # Add widgets to splitter
        splitter.addWidget(list_widget)
        splitter.addWidget(details_widget)
        splitter.setSizes([300, 400])  # Initial sizes
        
        content_layout.addWidget(splitter)
        main_layout.addWidget(content_frame, stretch=1)
        
        # Add a horizontal line separator
        separator2 = QFrame()
        separator2.setFrameShape(QFrame.Shape.HLine)
        separator2.setFrameShadow(QFrame.Shadow.Sunken)
        separator2.setStyleSheet("background-color: #444444; max-height: 1px; margin: 0 20px;")
        main_layout.addWidget(separator2)
        
        # Button row
        button_frame = QFrame()
        button_frame.setMaximumHeight(80)
        button_layout = QHBoxLayout(button_frame)
        button_layout.setContentsMargins(20, 10, 20, 10)
        
        self.report_button = QPushButton("⚠️ Report as Phishing")
        self.report_button.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        self.report_button.setMinimumHeight(40)
        self.report_button.clicked.connect(self.report_phishing)
        button_layout.addWidget(self.report_button)
        
        self.genuine_button = QPushButton("✓ Mark as Genuine")
        self.genuine_button.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        self.genuine_button.setMinimumHeight(40)
        self.genuine_button.clicked.connect(self.mark_genuine)
        button_layout.addWidget(self.genuine_button)
        
        self.new_emails_button = QPushButton("📨 Get New Emails")
        self.new_emails_button.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        self.new_emails_button.setMinimumHeight(40)
        self.new_emails_button.clicked.connect(self.generate_sample_emails)
        button_layout.addWidget(self.new_emails_button)
        
        button_layout.addStretch()
        
        tutorial_button = QPushButton("📚 Tutorial")
        tutorial_button.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        tutorial_button.setMinimumHeight(40)
        tutorial_button.clicked.connect(self.show_tutorial)
        button_layout.addWidget(tutorial_button)
        
        main_layout.addWidget(button_frame)
        
        # Status bar
        self.statusBar().showMessage("Ready")
        self.statusBar().setStyleSheet("color: #AAAAAA; font-size: 12px; padding: 5px;")
        
        # Set the main layout
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        
        # Create menu bar
        self.create_menu_bar()
    
    def create_menu_bar(self):
        menu_bar = self.menuBar()
        
        # File menu
        file_menu = menu_bar.addMenu("File")
        
        new_session = QAction("New Session", self)
        new_session.triggered.connect(self.new_session)
        file_menu.addAction(new_session)
        
        view_history = QAction("View History", self)
        view_history.triggered.connect(self.show_history)
        file_menu.addAction(view_history)
        
        file_menu.addSeparator()
        
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Help menu
        help_menu = menu_bar.addMenu("Help")
        
        tutorial_action = QAction("Tutorial", self)
        tutorial_action.triggered.connect(self.show_tutorial)
        help_menu.addAction(tutorial_action)
        
        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
    
    def show_welcome(self):
        # Create a custom dialog with consistent styling
        dialog = QInputDialog(self)
        dialog.setWindowTitle("Welcome")
        dialog.setLabelText("Enter your name to begin:")
        dialog.setTextValue("")
        dialog.setInputMode(QInputDialog.InputMode.TextInput)
        
        # Set dialog styling - fixed the label background
        dialog.setStyleSheet("""
            QInputDialog {
                background-color: #303030;
                color: white;
            }
            QInputDialog QLabel {
                background-color: #303030;
                color: white;
                border: none;
                padding: 5px;
            }
            QLineEdit {
                background-color: #232323;
                color: white;
                border: 1px solid #555555;
                border-radius: 3px;
                padding: 5px;
            }
        """)
        
        # Show dialog and get result
        ok = dialog.exec()
        
        if ok:
            name = dialog.textValue()
            self.user_manager.set_user_name(name if name else "User")
        else:
            self.user_manager.set_user_name("User")
        
        self.user_label.setText(f"User: {self.user_manager.user_name}")
        self.show_tutorial()
        self.generate_sample_emails()
    
    def show_tutorial(self):
        dialog = TutorialDialog(self)
        dialog.exec()
        self.tutorial_shown = True
    
    def generate_sample_emails(self):
        self.email_list.clear()
        emails = self.email_manager.generate_emails()
        
        for email in emails:
            if not email['removed']:
                item = EmailListItem(email)
                self.email_list.addItem(item)
        
        self.user_manager.total_emails = len(emails)
        self.update_status(f"Loaded {self.user_manager.total_emails} new emails. Review them carefully!")
        
        # Clear details
        self.details_text.clear()
        self.clear_attachments()
    
    def show_email_details(self, current, previous):
        if not current:
            return
        
        email = current.data(Qt.ItemDataRole.UserRole)
        if not email:
            return
        
        # Format email details with HTML - updated for dark mode
        details = f"""
        <div style="font-family: 'Segoe UI', sans-serif; color: #FFFFFF; background-color: #232323; padding: 15px; border-radius: 5px;">
            <p style="font-weight: bold; font-size: 18px; color: #4a86e8; margin-bottom: 15px;">{email['subject']}</p>
            <p style="margin-bottom: 8px;"><b>From:</b> {email['from']} &lt;{email['from_email']}&gt;</p>
            <p style="margin-bottom: 8px;"><b>Date:</b> {email['date']}</p>
            <hr style="border: none; border-top: 1px solid #444444; margin: 15px 0;">
            <div style="margin-top: 15px; line-height: 1.6; color: #EEEEEE;">
                {email['body'].replace('\n\n', '<br><br>').replace('\n', '<br>')}
            </div>
            {f'<p style="margin-top: 15px;"><a href="{email["link"]}" style="color: #4a86e8; text-decoration: underline;">Click here</a></p>' if email['link'] else ''}
        </div>
        """
        
        self.details_text.setHtml(details)
        
        # Update attachments display
        self.clear_attachments()
        
        if email['attachments']:
            for attachment in email['attachments']:
                attachment_btn = QPushButton(f"📎 {attachment}")
                attachment_btn.clicked.connect(lambda checked, a=attachment, p=email['is_phishing']: self.open_attachment(a, p))
                self.attachment_container.addWidget(attachment_btn)
        else:
            no_attachments = QLabel("No attachments")
            self.attachment_container.addWidget(no_attachments)
    
    def clear_attachments(self):
        # Clear attachment container
        while self.attachment_container.count():
            item = self.attachment_container.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
    
    def open_attachment(self, filename, is_phishing):
        if is_phishing:
            dangerous_extensions = ['.exe', '.bat', '.cmd', '.js', '.vbs', '.scr', '.jar']
            if any(filename.lower().endswith(ext) for ext in dangerous_extensions):
                msg_box = self.create_styled_message_box(
                    QMessageBox.Icon.Critical,
                    "Malware Detected!",
                    f"WARNING: The file '{filename}' appears to be malicious!\n\n"
                    "In a real scenario, this could have installed malware on your computer."
                )
                msg_box.exec()
            else:
                msg_box = self.create_styled_message_box(
                    QMessageBox.Icon.Warning,
                    "Suspicious Attachment",
                    f"Opening attachment '{filename}' from a phishing email.\n\n"
                    "Even if this file seems safe, it could still be dangerous."
                )
                msg_box.exec()
        else:
            msg_box = self.create_styled_message_box(
                QMessageBox.Icon.Information,
                "Safe Attachment",
                f"Opening legitimate attachment: {filename}\n\n"
                "This is a safe document from a trusted sender."
            )
            msg_box.exec()
    
    def open_email_link(self, item):
        email = item.data(Qt.ItemDataRole.UserRole)
        if not email:
            return
        
        if not email['link']:
            msg_box = self.create_styled_message_box(
                QMessageBox.Icon.Information,
                "No Link",
                "This email doesn't contain a clickable link."
            )
            msg_box.exec()
            return
        
        if email['is_phishing']:
            message = "You've been phished! This was a malicious link.\n\n"
            if email['red_flags']:
                message += "Red flags you missed:\n" + "\n".join(f"• {flag}" for flag in email['red_flags'])
            
            msg_box = self.create_styled_message_box(
                QMessageBox.Icon.Critical,
                "Hacked!",
                message
            )
            msg_box.exec()
            self.user_manager.score -= 15
            self.update_score_display()
        else:
            msg_box = self.create_styled_message_box(
                QMessageBox.Icon.Information,
                "Safe Link",
                "This is a legitimate link. You would now be taken to the official website."
            )
            msg_box.exec()
    
    def create_styled_message_box(self, icon, title, text):
        """Create a message box with consistent styling"""
        msg_box = CompactMessageBox(self)
        msg_box.setIcon(icon)
        msg_box.setWindowTitle(title)
        msg_box.setText(text)
        
        msg_box.setStyleSheet("""
            QMessageBox {
                background-color: #303030;
            }
            QLabel {
                color: white;
                background-color: #303030;
                border: none;
                max-width: 350px;
            }
            QPushButton {
                background-color: #2a82da;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 6px 12px;
                min-width: 80px;
            }
        """)
        
        return msg_box
    
    def report_phishing(self):
        current_item = self.email_list.currentItem()
        if not current_item:
            self.update_status("Please select an email to report")
            return
        
        current_index = self.email_list.currentRow()
        email = current_item.data(Qt.ItemDataRole.UserRole)
        if not email or email.get('evaluated'):
            self.update_status("You've already evaluated this email.")
            return

        if email['is_phishing']:
            self.user_manager.update_score(is_phishing=True, correct=True)
            message = "Good job! This was indeed a phishing email.\n\n"
            if email['red_flags']:
                message += "Red flags you identified:\n" + "\n".join(f"• {flag}" for flag in email['red_flags'])
            
            msg_box = self.create_styled_message_box(QMessageBox.Icon.Information, "Correct!", message)
            msg_box.exec()
        else:
            self.user_manager.update_score(is_phishing=False, correct=False)
            
            msg_box = self.create_styled_message_box(
                QMessageBox.Icon.Warning, 
                "Incorrect", 
                "This was actually a genuine email.\nBe careful not to report legitimate communications."
            )
            msg_box.exec()
        
        # Mark as evaluated and remove from list
        email['evaluated'] = True
        email['removed'] = True
        self.email_manager.remove_email(current_index)
        self.email_list.takeItem(current_index)
        
        self.update_score_display()
        self.check_round_completion()
    
    def mark_genuine(self):
        current_item = self.email_list.currentItem()
        if not current_item:
            self.update_status("Please select an email to mark as genuine")
            return
        
        current_index = self.email_list.currentRow()
        email = current_item.data(Qt.ItemDataRole.UserRole)
        if not email or email.get('evaluated'):
            self.update_status("You've already evaluated this email.")
            return

        if not email['is_phishing']:
            self.user_manager.update_score(is_phishing=False, correct=True)
            
            msg_box = self.create_styled_message_box(
                QMessageBox.Icon.Information, 
                "Correct!", 
                "Good job! This is indeed a legitimate email."
            )
            msg_box.exec()
        else:
            self.user_manager.update_score(is_phishing=True, correct=False)
            message = "Oops! This was actually a phishing email.\n\n"
            if email['red_flags']:
                message += "Red flags you missed:\n" + "\n".join(f"• {flag}" for flag in email['red_flags'])
            
            msg_box = self.create_styled_message_box(QMessageBox.Icon.Warning, "Incorrect", message)
            msg_box.exec()
        
        # Mark as evaluated and remove from list
        email['evaluated'] = True
        email['removed'] = True
        self.email_manager.remove_email(current_index)
        self.email_list.takeItem(current_index)
        
        self.update_score_display()
        self.check_round_completion()
    
    def update_score_display(self):
        self.score_label.setText(f"Score: {self.user_manager.score}")
        self.score_progress.setValue(max(0, min(200, self.user_manager.score)))
        self.stats_label.setText(
            f"Phishing Reported: {self.user_manager.phishing_emails_reported} | "
            f"Genuine Reported: {self.user_manager.genuine_emails_reported}"
        )
    
    def check_round_completion(self):
        # Check if there are any emails left in the list
        if self.email_list.count() == 0:
            self.user_manager.add_session_to_history(self.user_manager.total_emails)
            
            msg_box = self.create_styled_message_box(
                QMessageBox.Icon.Information,
                "Round Complete",
                f"You've evaluated all emails in this round!\n\n"
                f"Final Score: {self.user_manager.score}\n"
                f"Phishing Emails Identified: {self.user_manager.phishing_emails_reported}\n"
                f"Genuine Emails Identified: {self.user_manager.genuine_emails_reported}"
            )
            msg_box.exec()
    
    def new_session(self):
        self.user_manager.score = 0
        self.user_manager.phishing_emails_reported = 0
        self.user_manager.genuine_emails_reported = 0
        self.email_manager.restore_removed_emails()
        self.update_score_display()
        self.generate_sample_emails()
        self.update_status("New session started")
    
    def show_history(self):
        if not self.user_manager.history:
            msg_box = self.create_styled_message_box(
                QMessageBox.Icon.Information,
                "History",
                "No history available yet. Complete a round first!"
            )
            msg_box.exec()
            return
        
        history_dialog = QDialog(self)
        history_dialog.setWindowTitle("Your Performance History")
        history_dialog.setMinimumSize(700, 500)
        history_dialog.setStyleSheet("""
            QDialog {
                background-color: #303030;
            }
            QLabel {
                color: white;
            }
        """)
        
        layout = QVBoxLayout()
        
        history_label = QLabel("Your Training History")
        history_label.setFont(QFont("Segoe UI", 18, QFont.Weight.Bold))
        history_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(history_label)
        
        # Create a styled table for history
        history_text = QTextEdit()
        history_text.setReadOnly(True)
        
        # Format history as HTML table - updated for dark mode
        html = """
        <style>
            body {
                background-color: #232323;
                color: #FFFFFF;
                font-family: 'Segoe UI', sans-serif;
                padding: 15px;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
                border: 1px solid #444444;
                background-color: #2A2A2A;
            }
            th {
                background-color: #2a82da;
                color: white;
                padding: 12px;
                text-align: left;
                font-weight: bold;
                font-size: 14px;
            }
            td {
                padding: 10px;
                border-bottom: 1px solid #444444;
                color: #EEEEEE;
            }
            tr:nth-child(even) {
                background-color: #333333;
            }
            tr:hover {
                background-color: #3A3A3A;
            }
            .score-cell {
                font-weight: bold;
                color: #2ecc71;
            }
            .date-cell {
                color: #cccccc;
                font-style: italic;
            }
            .header {
                font-size: 24px;
                color: #4a86e8;
                text-align: center;
                margin-bottom: 20px;
                font-weight: bold;
            }
            .summary {
                background-color: #2a2a2a;
                border-radius: 5px;
                padding: 15px;
                margin-bottom: 20px;
                border: 1px solid #444444;
            }
            .stat {
                font-weight: bold;
                color: #4a86e8;
            }
        </style>
        
        <div class="header">Performance Summary</div>
        
        <div class="summary">
            <p>Total Sessions: <span class="stat">{len(self.user_manager.history)}</span></p>
            <p>Average Score: <span class="stat">{sum(session['score'] for session in self.user_manager.history) / len(self.user_manager.history):.1f}</span></p>
            <p>Phishing Emails Caught: <span class="stat">{sum(session['phishing_caught'] for session in self.user_manager.history)}</span></p>
        </div>
        
        <table>
            <tr>
                <th>Date</th>
                <th>Score</th>
                <th>Accuracy</th>
                <th>Phishing Caught</th>
                <th>Genuine Correct</th>
            </tr>
        """
        
        for session in self.user_manager.history:
            html += f"""
            <tr>
                <td class="date-cell">{session['date']}</td>
                <td class="score-cell">{session['score']}</td>
                <td>{session['accuracy']:.1f}%</td>
                <td>{session['phishing_caught']}</td>
                <td>{session['genuine_correct']}</td>
            </tr>
            """
        
        html += "</table>"
        history_text.setHtml(html)
        layout.addWidget(history_text)
        
        # Close button
        close_button = QPushButton("Close")
        close_button.clicked.connect(history_dialog.accept)
        
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(close_button)
        button_layout.addStretch()
        
        layout.addLayout(button_layout)
        history_dialog.setLayout(layout)
        
        history_dialog.exec()
    
    def show_about(self):
        msg_box = self.create_styled_message_box(
            QMessageBox.Icon.Information,
            "About",
            "Advanced Phishing Awareness Simulator\n\n"
            "A gamified educational tool to help users identify and avoid phishing attacks.\n\n"
            "Learn to protect yourself and your organization from the most common cyber threat."
        )
        msg_box.exec()
    
    def update_status(self, message):
        status_bar = self.statusBar()
        status_bar.showMessage(message)

class CompactMessageBox(QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumWidth(400)
        
        # Adjust grid layout spacing
        grid_layout = self.layout()
        if isinstance(grid_layout, QGridLayout):
            # Reduce spacing between icon and text
            grid_layout.setHorizontalSpacing(10)
            grid_layout.setContentsMargins(15, 15, 15, 15)
    
    def resizeEvent(self, event):
        super().resizeEvent(event)
        # Ensure the dialog isn't too wide
        if self.width() > 500:
            self.resize(500, self.height()) 