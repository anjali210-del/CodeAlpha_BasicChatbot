# Function 1: Welcome message
def welcome():
    print("\n" + "=" * 45)
    print("       WELCOME TO FRIENDLY BUDDY!")
    print("=" * 45)
    print("Hello! I am Friendly Buddy.")
    print("I am your personal chatbot.")
    print("Let's have a friendly conversation!")
    print("\nType 'help' to see what I can do.")
    print("Type 'bye' to exit the chatbot.")
    print("=" * 45)


# Function 2: Generate chatbot responses
def get_response(user_input):

    if user_input == "hello":
        return "Hi! Nice to meet you!"

    elif user_input == "hi":
        return "Hello! How can I help you?"

    elif user_input == "hey":
        return "Hey there! How are you today?"

    elif user_input == "how are you":
        return "I'm fine, thanks! How are you?"

    elif user_input == "what is your name":
        return "My name is Friendly Buddy!"

    elif user_input == "what can you do":
        return "I can chat with you and answer simple questions!"

    elif user_input == "thank you" or user_input == "thanks":
        return "You're very welcome!"

    elif user_input == "good morning":
        return "Good morning! Have a wonderful day!"

    elif user_input == "good afternoon":
        return "Good afternoon! Hope you are having a great day!"

    elif user_input == "good evening":
        return "Good evening! Nice to see you!"

    elif user_input == "good night":
        return "Good night! Sweet dreams!"

    elif user_input == "help":
        return (
            "Here are some messages you can try:\n"
            "hello, hi, hey, how are you,\n"
            "what is your name, what can you do,\n"
            "thank you, good morning, good night, bye."
        )

    elif user_input == "bye":
        return "Goodbye! It was lovely chatting with you!"

    else:
        return "Sorry, I don't understand that. Type 'help' for suggestions."


# Function 3: Main chatbot conversation
def chatbot():

    welcome()

    while True:

        user_input = input("\nYou: ").strip().lower()

        # Check for empty input
        if user_input == "":
            print("Buddy: Please type something!")
            continue

        # Get the chatbot response
        response = get_response(user_input)

        # Display the response
        print("Buddy:", response)

        # Exit the chatbot
        if user_input == "bye":
            print("\nThank you for chatting with Friendly Buddy!")
            print("Have a wonderful day!")
            break


# Function 4: Start the program
if __name__ == "__main__":
    chatbot()

