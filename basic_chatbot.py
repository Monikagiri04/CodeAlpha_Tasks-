def chatbot():
    print("Chatbot started! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Bot: Hi!")

        elif user_input == "hi":
            print("Bot: Hello there!")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user_input == "what is your name":
            print("Bot: I am a simple chatbot.")

        elif user_input == "who created you":
            print("Bot: I was created using Python.")

        elif user_input == "what can you do":
            print("Bot: I can chat with you using simple rules.")

        elif user_input == "good morning":
            print("Bot: Good morning! Have a great day.")

        elif user_input == "good evening":
            print("Bot: Good evening! Hope your day was good.")

        elif user_input == "good night":
            print("Bot: Good night! Sweet dreams.")

        elif user_input == "thank you":
            print("Bot: You're welcome!")

        elif user_input == "thanks":
            print("Bot: Happy to help!")

        elif user_input == "help":
            print("Bot: You can say hello, ask how I am, or say bye.")

        elif user_input == "where are you from":
            print("Bot: I live inside this computer.")

        elif user_input == "are you real":
            print("Bot: I am a program, not a human.")

        elif user_input == "do you like python":
            print("Bot: Yes! Python is my favorite language.")

        elif user_input == "what is python":
            print("Bot: Python is a popular programming language.")

        elif user_input == "how old are you":
            print("Bot: I do not have an age.")

        elif user_input == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()
