from transformers import pipeline

# Initialize chatbot model
chat_model = pipeline("text-generation", model="gpt2")

# Test the chatbot
response = chat_model("Hello, how can I help you today?")
print(response)
