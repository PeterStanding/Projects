from openai import OpenAI

client = OpenAI()
conversation = []

prompt = "Can you tell me a fact about London?"
# Create a chat request
def send_message(message, user_message):
    '''
    n                   = Number of Responses Wanted
    max_tokens          = Sets hard limit on number of tokens that can be created
                            --> 100
    temperature         = Controls Randomness 
                            --> Lower the value, more predictable
                            --> 0.7
    presence_penalty    = Penalizing AI for using words that have already appeared in the conversation
                            --> Lower the value, AI less discouraged from repeating words
                            --> 0.6
    frequency_penalty   = Helps Reduce repetition in the responses 
                            --> Lower the value, allows for more repetition
                            --> 0.3
    '''
    conversation.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model = "gpt-4",
        messages = [{"role":"user", "content":message}],
        # Total number of responses
        n = 3
    )
    
    reply = response.choices[0].message.content.strip()
    conversation.append({"role": "assistant", "content": reply})
    
    return reply

# Iterate over the Conversation History
def print_conversation_history(convo):
    for msg in convo:
        print("Role : ", msg['role'], " --> ", msg['content'])

# Get first response
reply = send_message(conversation, prompt)
print("Assistant:", reply)

# Add a follow-up question
prompt2 = "How long is the Thames?"

# Get response with conversation context
follow_up_reply = send_message(conversation, prompt2)
print("Assistant follow-up:", follow_up_reply)