import random

# The answers to the queries
answers = {
    'What is XYZ?': 'XYZ is a company that provides XYZ services.',
    'What does XYZ do?': 'XYZ helps customers find solutions to their problems.',
    'Where is XYZ located?': 'XYZ is located in ABC city.',
    'What are the benefits of using XYZ?': 'XYZ provides a quick and easy way to find solutions to your problems.'
}

# Generate a response
def generate_response(question):
    if question in answers:
        return answers[question]
    else:
        return random.choice(['I am not sure I understand.', 'Can you give me more information?', 'Can I help you with something else?'])

# Start the conversation
question = input('Welcome to XYZ. How can I help you? ')
response = generate_response(question)

while response != 'Goodbye':
    print(response)
    question = input('Is there anything else I can help you with? ')
    response = generate_response(question)

print('Goodbye!')