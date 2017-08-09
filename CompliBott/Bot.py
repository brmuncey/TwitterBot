from CompliBott.BotConnector import BotConnector
from CompliBott.Message import Message


class Bot(object):
    connector = ""
    controller = ""
    db = ""

    def __init__(self):
        print("Bot Created")
        self.connector = BotConnector()
        self.db = self.connector.get_firebase_db()
        self.controller = self.connector.get_twitter_controller()
        self.check_for_mentions()

    def check_for_mentions(self):
        messages = []
        for dm in self.controller.GetDirectMessages():
            messages.append(Message(str(dm)))
