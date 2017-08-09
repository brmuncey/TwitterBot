from CompliBott.BotBuilder import BotBuilder
from CompliBott.Message import Message
from CompliBott.Response import Response


class Bot(object):
    connector = ""
    controller = ""
    messages = []

    def __init__(self):
        print("Bot Created")
        self.connector = BotBuilder()
        self.controller = self.connector.get_twitter_controller()
        self.check_for_messages()
        self.reply_to_messages()

    def check_for_messages(self):
        for dm in self.controller.GetDirectMessages():
            self.messages.append(Message(str(dm)).get_message())

    def reply_to_messages(self):
        unique_sender_text = {}
        for m in self.messages:
            if unique_sender_text.get(m.sender_screen_name) is None:  # Unique Sender
                unique_sender_text[m.sender_screen_name] = m.text
            else:  # Duplicate Sender
                unique_sender_text[m.sender_screen_name] = m.text + " " + unique_sender_text[m.sender_screen_name]

        for user in unique_sender_text:
            self.parse_text(unique_sender_text[user])

            # clear dm from users that are responded to

    def parse_text(self, text):
        response = Response(text)
