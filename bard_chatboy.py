import google.generativeai as genai

API_KEY = "AIzaSyB91-4FG33qNy-Y-MHgXRtHBm7hDTxaFYA"

genai.configure(api_key=API_KEY)

# Use the correct model name that supports 'generateMessage'
model = genai.GenerativeModel('gemini-1.5-flash-001')

def chat_with_bard():
    print("Chatbot: Hello! I’m Bard. Type 'exit' to end the chat.\n")
    chat = model.start_chat(history=[])
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Chatbot: Goodbye!")
            break
        try:
            response = chat.send_message(user_input)
            print("Chatbot:", response.text)
        except Exception as e:
            print("Error:", str(e))
            break

if __name__ == "__main__":
    chat_with_bard()
