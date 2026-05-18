from openai import OpenAI
import uuid
from chat import ChatManager

client = OpenAI()
conversation = []
chat_sessions = {}

prompt = "Can you tell me a fact about London?"
# Create a chat request
def send_message(chat_id, user_message):
    if chat_id not in chat_sessions:
        raise ValueError("Chat Sessions not found")
    
    chat_sessions[chat_id].append({"role": "user", "content": user_message})
    response = client.chat.completions.create(
        model="gpt-4",
        messages = chat_sessions[chat_id]
    )
    
    answer = response.choices[0].message.content.strip()
    chat_sessions[chat_id].append({"role": "assistant", "content": answer})
    return answer
# Create a new Chat Session with a Unique Identifier
def create_Chat():
    chat_id = str(uuid.uuid4())  # Create unique session identifier
    chat_sessions[chat_id] = []  # Initialize empty conversation history
    chat_sessions[chat_id].append(system_prompt)  # Add system prompt to conversation history
    return chat_id
# Iterate over the Conversation History
def print_conversation_history(convo):
    for msg in convo:
        print("Role : ", msg['role'], " --> ", msg['content'])
# Read file for the System Prompt
def load_system_prompt(file_path: str) -> str:
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except Exception as e:
        print(f"Error loading system prompt: {e}")
        return "You are a helpful Assistant"

system_prompt = load_system_prompt('system_prompt.txt')
# Define a common system prompt for all conversations
system_prompt = {
    "role": "system",
    "content": "You are a friendly and efficient customer service attendant eager to assist customers with their inquiries and concerns."
}

chat_id = create_Chat()
manager = ChatManager()

print("Response:", send_message(chat_id, "I'm having trouble with my recent order. Can you help me track it?"))

# Print the entire conversation history for the chat session
print("\nConversation History:")
for message in chat_sessions[chat_id]:
    print(f"- {message['role'].capitalize()}: {message['content']}")
'''
conversation = [
    # System message defines the AI's behavior and tone
    {"role": "system", "content": system_prompt},
    # User message contains the actual question
    {"role": "user", "content": "What's a popular type of pizza?"},
]
'''