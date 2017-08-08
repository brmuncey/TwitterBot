from src.BotConnector import BotConnector


class Bot(object):
    name = ""

    def __init__(self, name):
        print("Bot Launched")
        self.name = name
        connector = BotConnector()

    def get_name(self) -> str:
        return self.name
