print("===== SIMPLE CHATBOT =====")
print("Type 'bye' to exit\n")

while True:

    user_input = input("You: ").lower()

    # Greeting
    if user_input == "hi" or user_input == "hello":
        print("Bot: Hello! How can I help you?")

    # Asking name
    elif "your name" in user_input:
        print("Bot: I am a Rule-Based Chatbot.")

    # Asking about AI
    elif "ai" in user_input:
        print("Bot: AI means Artificial Intelligence.")

    # Asking about college
    elif "college" in user_input:
        print("Bot: College life is very interesting!")

    # Asking time
    elif "time" in user_input:
        print("Bot: Sorry, I cannot tell real time now.")

    # Thank you
    elif "thank" in user_input:
        print("Bot: You're welcome!")

    # Exit
    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    # Unknown input
    else:
        print("Bot: Sorry, I don't understand that.")
