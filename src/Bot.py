from src.Login import Login


def login_to_twitter(username, password):
    print("Bot Login" + username + password)

    # connect to twitter api


class Bot(object):
    name = ""

    def __init__(self, name):
        print("Bot Launched")
        self.name = name
        login = Login()
        login_to_twitter(login.get_username(), login.get_password())

    def get_name(self) -> str:
        return self.name
