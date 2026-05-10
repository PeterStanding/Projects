from openai import OpenAI

client = OpenAI()

# Define a simple user message
prompt = "Hi, can you tell me a joke?"

# Create a chat request
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

reply = response.choices[0].message.content.strip()

print("Prompt: ", prompt)
print("Response", reply)

#Loop through the first 3 choices and print them
print("Prompt:", prompt)
for c in response.choices:
    print("Response:", c.message.content.strip())
