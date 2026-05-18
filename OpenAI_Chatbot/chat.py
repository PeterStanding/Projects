class ChatManager:
    def __init__(self):
        self.chats = {}  # user_id -> chat_id -> chat_data
    # Creates a Chat for the User with unique ID
    def create_chat(self, user_id, chat_id, system_prompt):
        if user_id not in self.chats:
            self.chats[user_id] = {}
        
        self.chats[user_id][chat_id] = {
            'system_prompt': system_prompt,
            'messages': []
        }
    
    # Returns all Chats for that user
    def get_chat(self, user_id, chat_id):
        return self.chats.get(user_id, {}).get(chat_id)
    
    # Adds a new Chat to the Conversation
    def add_message(self, user_id, chat_id, role, content):
        if chat := self.get_chat(user_id, chat_id):
            chat['messages'].append({"role":role, "content":content})
    
    # Returns the Conversation between the User and Bot
    def get_conversation(self, user_id, chat_id):
        if chat := self.get_chat(user_id, chat_id):
            system_message = {"role":"system", "content":chat['system_prompt']}
            return [system_message] + chat['messages']
        return []