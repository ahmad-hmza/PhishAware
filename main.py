import sys
import os
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QColor, QIcon, QPixmap, QImage
from PyQt6.QtCore import Qt
from ui import EmailSimulator

# Initialize the application
app = QApplication(sys.argv)

# Set app icon if available
icon_path = "icon.png"  # Use the icon.png file
if os.path.exists(icon_path):
    # Load the icon as QImage
    image = QImage(icon_path)
    # Invert the colors
    image.invertPixels()
    
    # Convert back to pixmap and create icon
    pixmap = QPixmap.fromImage(image)
    icon = QIcon(pixmap)
    app.setWindowIcon(icon)

# Set global application style
app.setStyle("Fusion")

# Set application-wide stylesheet for basic dark theme
app.setStyleSheet("""
    QWidget {
        background-color: #303030;
        color: white;
        font-family: 'Segoe UI', Arial, sans-serif;
    }
    QPushButton {
        background-color: #2a82da;
        color: white;
        border: none;
        border-radius: 4px;
        padding: 8px 16px;
        min-height: 30px;
    }
    QFrame {
        background-color: #232323;
        border-radius: 6px;
    }
    QListWidget, QTextEdit {
        background-color: #232323;
        border: 1px solid #555555;
    }
    QProgressBar {
        border: none;
        background-color: #444444;
        text-align: center;
    }
    QProgressBar::chunk {
        background-color: #2ecc71;
    }
    
    /* Custom Scrollbar Styling */
    QScrollBar:vertical {
        border: none;
        background-color: #2A2A2A;
        width: 14px;
        margin: 15px 0 15px 0;
        border-radius: 7px;
    }
    QScrollBar::handle:vertical {
        background-color: #3A82DA;
        min-height: 30px;
        border-radius: 7px;
    }
    QScrollBar::handle:vertical:hover {
        background-color: #4A92EA;
    }
    QScrollBar::handle:vertical:pressed {
        background-color: #2A72CA;
    }
    QScrollBar::sub-line:vertical {
        border: none;
        background-color: #3A3A3A;
        height: 15px;
        border-top-left-radius: 7px;
        border-top-right-radius: 7px;
        subcontrol-position: top;
        subcontrol-origin: margin;
    }
    QScrollBar::add-line:vertical {
        border: none;
        background-color: #3A3A3A;
        height: 15px;
        border-bottom-left-radius: 7px;
        border-bottom-right-radius: 7px;
        subcontrol-position: bottom;
        subcontrol-origin: margin;
    }
    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
        background: none;
        height: 15px;
        width: 15px;
    }
    QScrollBar::up-arrow:vertical {
        image: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAiIGhlaWdodD0iMTAiIHZpZXdCb3g9IjAgMCAyMCAyMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMTAgNUwxOSAxNEg1eiIgZmlsbD0iI2FhYSIvPjwvc3ZnPg==);
    }
    QScrollBar::down-arrow:vertical {
        image: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAiIGhlaWdodD0iMTAiIHZpZXdCb3g9IjAgMCAyMCAyMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMTAgMTVMMTkgNkg1eiIgZmlsbD0iI2FhYSIvPjwvc3ZnPg==);
    }
    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
        background: none;
    }
    
    /* Horizontal Scrollbar */
    QScrollBar:horizontal {
        border: none;
        background-color: #2A2A2A;
        height: 14px;
        margin: 0 15px 0 15px;
        border-radius: 7px;
    }
    QScrollBar::handle:horizontal {
        background-color: #3A82DA;
        min-width: 30px;
        border-radius: 7px;
    }
    QScrollBar::handle:horizontal:hover {
        background-color: #4A92EA;
    }
    QScrollBar::handle:horizontal:pressed {
        background-color: #2A72CA;
    }
    QScrollBar::sub-line:horizontal {
        border: none;
        background-color: #3A3A3A;
        width: 15px;
        border-top-left-radius: 7px;
        border-bottom-left-radius: 7px;
        subcontrol-position: left;
        subcontrol-origin: margin;
    }
    QScrollBar::add-line:horizontal {
        border: none;
        background-color: #3A3A3A;
        width: 15px;
        border-top-right-radius: 7px;
        border-bottom-right-radius: 7px;
        subcontrol-position: right;
        subcontrol-origin: margin;
    }
    QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {
        background: none;
        width: 15px;
        height: 15px;
    }
    QScrollBar::left-arrow:horizontal {
        image: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAiIGhlaWdodD0iMTAiIHZpZXdCb3g9IjAgMCAyMCAyMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNNSAxMEwxNCAxOVYxeiIgZmlsbD0iI2FhYSIvPjwvc3ZnPg==);
    }
    QScrollBar::right-arrow:horizontal {
        image: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAiIGhlaWdodD0iMTAiIHZpZXdCb3g9IjAgMCAyMCAyMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMTUgMTBMNiAxVjE5eiIgZmlsbD0iI2FhYSIvPjwvc3ZnPg==);
    }
    QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
        background: none;
    }
    
    QInputDialog {
        background-color: #303030;
    }
    QInputDialog QLabel {
        color: white;
        background-color: #303030;
        border: none;
    }
    QLineEdit {
        background-color: #232323;
        color: white;
        border: 1px solid #555555;
        border-radius: 3px;
        padding: 5px;
    }
    QDialog {
        background-color: #303030;
    }
    QMessageBox {
        background-color: #303030;
    }
    QMessageBox QLabel {
        color: white;
        background-color: #303030;
        border: none;
    }
    QMessageBox QPushButton {
        min-width: 100px;
    }
""")

# Create the simulator
simulator = EmailSimulator()
simulator.show()

# Run the application
sys.exit(app.exec())