def get_response(user_input):
   
    user_input = user_input.lower().strip()

    if "hello" in user_input or "hi" in user_input:
        response = "Hi!"
    elif "how are you" in user_input:
        response = "I'm fine, thanks!"
    elif "bye" in user_input:
        response = "Goodbye!"
    else:
        response = "Sorry, I didn't quite understand that. Try hello, how are you, or bye."

    return response

def run_chatbot():
  
    print("Chatbot: Hi! Type 'bye' anytime to end our chat.")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Chatbot:", response)

        if "bye" in user_input.lower():
            break


if __name__ == "__main__":
    run_chatbot()
