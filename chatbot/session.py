class ChatSession:
    def __init__(self):
        self.history = []

    def add_message(self, sender, message):
        self.history.append((sender, message))

    def clear(self):
        self.history = []
