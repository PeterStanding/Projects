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

    def process_message(self, user_id: str, chat_id: str, message: str) -> str:
        # Step 1: Retrieve the chat
        chat = self.chat_manager.get_chat(user_id, chat_id)
        if not chat:
            raise ValueError("Chat not found")
        
        # Step 2: Add user message to chat history
        self.chat_manager.add_message(user_id, chat_id, "user", message)
        
        try:
            # Step 3: Get AI response
            conversation = self.chat_manager.get_conversation(user_id, chat_id)
            
            response = self.openai_client.chat.completions.create(
                model="gpt-4",
                messages=conversation,
                temperature=0.7,
                max_tokens=500
            )
            
            ai_message = response.choices[0].message.content
            
            # Step 4: Add AI response to chat history
            self.chat_manager.add_message(user_id, chat_id, "assistant", ai_message)
            
            return ai_message    
        except Exception as e:
            # Step 5: Handle errors
            raise RuntimeError(f"Error getting AI response: {str(e)}")