from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication
import sys
from backend import Chatbot
import threading

class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chat GPT")
        self.setMinimumSize(700, 500)

        # Add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)
        # Pixels(distane from left border, upper border, width , height)

        # Add the input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)
        self.input_field.returnPressed.connect(self.send_message)
        # 10 (distance from upper chat area) + height 320 + 10 for distance = 340

        # Add the button
        self.btn_send = QPushButton("Send", self)
        self.btn_send.setGeometry(500, 345, 85, 30)
        self.btn_send.clicked.connect(self.send_message)

        self.show()

        self.chatbot = Chatbot()


    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"<p style='color:#333333'><b>Me:</b> {user_input}</p>")
        self.input_field.clear()

        thread = threading.Thread(target=self.get_bot_response,args=(user_input,))
        thread.start()

    def get_bot_response(self, user_input):
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(f"<p style= 'color:#333333; background-color:powderblue'>ChatBot:{response}</p>")

app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())
