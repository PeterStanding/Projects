from openai import OpenAI

client = OpenAI()

# Define a simple user message
prompt = "Hi, can you tell me a joke?"

# Create a chat request
response = client.chat.completions.create(
    model = "gpt-4",
    message = [{"role":"user", "content":prompt}]
)

reply = response.choices[0].message.content.strip()

print("Prompt: ", prompt)
print("Response", reply)