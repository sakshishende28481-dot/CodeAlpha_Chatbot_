import datetime

def chatbot():
    print("Chatbot: Hello! I'm your friendly chatbot.")
    print("Chatbot: You can say hello, ask my name, ask the time, or say bye.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hello", "hi", "hey"]:
            print("Chatbot: Hi there! ")

        elif user_input == "how are you":
            print("Chatbot: I'm doing great! Thanks for asking.")

        elif user_input == "what is your name":
            print("Chatbot: I'm a basic rule-based chatbot.")

        elif user_input == "who created you":
            print("Chatbot: I was created by a student using Python.")

        elif user_input == "what can you do":
            print("Chatbot: I can answer simple questions and chat with you.")

        elif user_input == "help":
            print("Chatbot: Try saying hello, asking my name, or asking the time.")

        elif user_input == "what is the current time":
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Chatbot: Current time is {current_time}")

        elif user_input == "what is the day":
            day_name = datetime.datetime.now().strftime("%A")
            print(f"Chatbot: Today is {day_name}")

        elif user_input in ["thanks", "thank you"]:
            print("Chatbot: You're welcome! ")

        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a great day ")
            break

        else:
            print("Chatbot: Hmm… I don't understand that yet.")
            print("Chatbot: Can you ask something simple?")

# Start chatbot
chatbot()
