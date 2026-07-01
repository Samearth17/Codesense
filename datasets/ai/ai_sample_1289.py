class Message(object):
    def __init__(self,subject, sender, receiver, body):
        self.subject = subject
        self.sender = sender
        self.receiver = receiver
        self.body = body

class MessageStore(object):
    def __init__(self, messages):
        self.messages = messages
        self.indexes = {}

    def addMessage(self,message):
        message_id = len(self.messages) + 1
        self.messages.append(message)
        self.indexes[message.subject] = message_id

    def getMessage(self,message_id):
        if message_id in self.indexes.values():
            return self.messages[message_id - 1]  # Array index is 1 lower than message_id
        else:
            return None