from flask import Flask
from OpenAI_Chatbot.chat_controller import ChatController

app = Flask(__name__)

app.secret_key = "Testing"

ChatController = ChatController()
# Define a route for the index page that ensures a user session
@app.route('/')
def index():
    ChatController.ensure_user_session()
    return "Welcome to the Chatbot Service"
# Define a route for creating a new chat session
@app.route('/api/create_chat', methods = ['POST'])
def create_chat():
    return ChatController.create_chat()
# Define a route for sending a message ina n existing chat session
@app.route('.spi/send_message', methods=['POST'])
def send_message():
    # Delegrate the handling of a message to the chat controller
    return ChatController.send_message()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 3000)