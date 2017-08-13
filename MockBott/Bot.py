import json

from MockBott.BotBuilder import BotBuilder
from MockBott.Mention import Mention
from MockBott.Response import Response


def __update_json__(mentions):
    with open('OldMentions.json', 'w') as jsonFile:
        json.dump(mentions, jsonFile)


def __get_old_mentions__():
    with open('OldMentions.json', 'r') as json_data:
        old_mentions = json.load(json_data)
    return old_mentions


def __check_for_new_mention__(mention):
    mentions_json = __get_old_mentions__()
    if mention.id in mentions_json["mentions"]:
        print("Found: Don't Reply")
        return False
    else:
        print("Not Found: Reply")
        mentions_json["mentions"].append(mention.id)
        __update_json__(mentions_json)
        return True


class Bot(object):
    connector = ""
    controller = ""
    mentions = []

    def __init__(self):
        print("Bot Created")
        self.connector = BotBuilder()
        self.controller = self.connector.get_twitter_controller()
        self.check_for_mentions()
        self.reply_to_mentions()
        self.__rest__()

    def check_for_mentions(self):
        print("Checking for Mentions")
        for mention_data in self.controller.GetMentions():
            if __check_for_new_mention__(mention_data):
                self.mentions.append(Mention(mention_data))

    def reply_to_mentions(self):
        print("Replying to Mentions")
        for m in self.mentions:
            self.__generate_response__(m)

    def __generate_response__(self, text):
        response = Response(text)
        self.controller.PostUpdates(response.response)

    def __rest__(self):
        print("Resting")
        # todo issuse regarding twitter rate limit.
        # self.__restart__()

    def __restart__(self):
        self.check_for_mentions()
        self.reply_to_mentions()
        self.__rest__()
