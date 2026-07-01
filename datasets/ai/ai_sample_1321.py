def respond(message):
 bot_template = "I'm sorry, I don't understand. Could you try rephrasing that?"
 user_template = "USER: {message}\nBOT: {response}"

 response = bot_template
 
 if 'hello' in message:
 response = "Hi! How can I help you?"
 elif 'your name' in message:
 response = "My name is Chatbot!"
 
 print(user_template.format(message=message, response=response))


if __name__ == "__main__":
 respond("Hello")
 respond("What is your name?")