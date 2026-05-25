print("Welcome to Simple Chatbot!")
print("Type 'bye' to end the chat.\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hello! How can I help you?")

  
    elif "your name" in user_input:
        print("Bot: My name is RuleBot.")

   
    elif "internship" in user_input:
        print("Bot: Internships help improve your practical skills and experience.")

  
    elif "python" in user_input:
        print("Bot: Python is a simple and powerful programming language.")

   
    elif "weather" in user_input:
        print("Bot: I cannot check live weather, but I hope it's a good day!")

   
    elif "thank you" in user_input or "thanks" in user_input:
        print("Bot: You're welcome!")

   
    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
