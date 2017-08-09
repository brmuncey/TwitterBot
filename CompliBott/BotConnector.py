import pyrebase
import twitter


class BotConnector(object):
    db = ""
    twitter_controller = ""

    def __init__(self):
        print("Building Bot Components")
        self.__connect_to_firebase()
        self.__connect_to_twitter()

    def __connect_to_twitter(self):
        api = twitter.Api(consumer_key=self.__get_consumer_key(),
                          consumer_secret=self.__get_consumer_secret(),
                          access_token_key=self.__get_access_token_key(),
                          access_token_secret=self.__get_access_token_secret())
        self.twitter_controller = api

    def __connect_to_firebase(self):
        config = {
            "apiKey": "AIzaSyDJH5BZQtgs3AAIdSxjK1g0pEOoMB5gmyc",
            "authDomain": "complibott-dbd28.firebaseapp.com",
            "databaseURL": "https://complibott-dbd28.firebaseio.com/",
            "storageBucket": "gs://complibott-dbd28.appspot.com"
        }

        self.db = pyrebase.initialize_app(config).database()

    def __get_consumer_key(self):
        return self.db.child("Credentials").child("consumer_key").get().val()

    def __get_consumer_secret(self):
        return self.db.child("Credentials").child("consumer_secret").get().val()

    def __get_access_token_key(self):
        return self.db.child("Credentials").child("access_token_key").get().val()

    def __get_access_token_secret(self):
        return self.db.child("Credentials").child("access_token_secret").get().val()

    def get_twitter_controller(self):
        return self.twitter_controller

    def get_firebase_db(self):
        return self.db