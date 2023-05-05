from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication
import sys

class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chat GPT")
        self.setMinimumSize(700,500)

        # Add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10,10,480,320)
        self.chat_area.setReadOnly(True)
        # Pixels(distane from left border, upper border, width , height)

        # Add the input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10,340,480,40)
        # 10 (distance from upper chat area) + height 320 + 10 for distance = 340

        # Add the button
        self.btn_send = QPushButton("Send", self)
        self.btn_send.setGeometry(500,345,85,30)

        self.show()

class Chatbot:
    pass

app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())
