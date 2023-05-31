
import random

# Dictionary of predefined responses
responses = {
    "greeting": ["Hello!", "Hi there!", "Welcome! How can I assist you today?"],
    "goodbye": ["Goodbye!", "See you later!", "Have a great day!"],
    "thanks": ["You're welcome!", "No problem!", "Happy to help!"],
    "default": ["I'm sorry, I didn't understand. Could you please rephrase?", 
                "Apologies, I couldn't grasp that. Can you please provide more details?"]
}

def get_response(message):
    # Clean the message (remove punctuation and convert to lowercase)
    cleaned_message = message.lower().strip()
    
    # Check for keywords in the message to determine the appropriate response
    if "hello" in cleaned_message or "hi" in cleaned_message:
        return random.choice(responses["greeting"])
    elif "goodbye" in cleaned_message or "bye" in cleaned_message:
        return random.choice(responses["goodbye"])
    elif "thank you" in cleaned_message or "thanks" in cleaned_message:
        return random.choice(responses["thanks"])
    else:
        return random.choice(responses["default"])

# Chat loop
print("Chatbot: Hi! How can I assist you today?")
while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)
