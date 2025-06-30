def chatbot_response(user_input):
    # Convert the input to lowercase to handle case insensitivity
    user_input = user_input.lower()

    # Define some simple rules using if-else statements
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a program, but thanks for asking! How about you?"
    elif "your name" in user_input:
        return "I'm a rule-based chatbot created to assist you!"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I didn't understand that. Can you please rephrase?"

# Example of usage
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")
