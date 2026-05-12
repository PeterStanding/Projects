from openai import OpenAI

client = OpenAI()

# Create a chat request
def send_message(message):
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
    response = client.chat.completions.create(
        model = "gpt-4",
        messages = [{"role":"user", "content":prompt}],
        # Total number of responses
        n = 3
    )

    return response.choices[0].message.content.strip()

# Iterate over the Conversation History
def conversation_history(convo):
    for msg in convo:
        print("Role : ", msg['role'], " --> ", msg['content'])
conversation = [
    {"role": "user", "content": "What's the capital of France?"}
]

# Get first response
reply = send_message(conversation)
print("Assistant:", reply)

# Append the Response to the History
conversation.append({"role": "assistant", "content": reply})
conversation.append({"role": "user", "content" : "Is it a large City?"})

follow_up = send_message(conversation)
print("Assistant: ", follow_up)
