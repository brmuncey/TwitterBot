import json

from CompliBott.BotBuilder import BotBuilder
from CompliBott.Mention import Mention
from CompliBott.Response import Response


def __update_json__(mentions):
    with open('OldMentions.json', 'w') as jsonFile:
        json.dump(mentions, jsonFile)


def __get_old_mentions__():
    with open('OldMentions.json', 'r') as json_data:
        old_mentions = json.load(json_data)
    return old_mentions


def parse_text(text):
    response = Response(text)


def __check_for_new_mention__(mention):
    mentions_json = __get_old_mentions__()
    if mention.id in mentions_json["mentions"]:
        print("Found")
        return False
    else:
        print("Not Found")
        mentions_json["mentions"].append(mention.id)
        __update_json__(mentions_json)
        print(mentions_json)
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
        # self.reply_to_messages()

    def check_for_mentions(self):
        print("Checking for Mentions")
        for mention_data in self.controller.GetMentions():
            if __check_for_new_mention__(mention_data):
                self.mentions.append(Mention(mention_data))

    def reply_to_mentions(self): #todo
        unique_sender_text = {}
        for m in self.mentions:
            print(m)
            if unique_sender_text.get(m.sender_screen_name) is None:  # Unique Sender
                unique_sender_text[m.sender_screen_name] = m.text
            else:  # Duplicate Sender
                unique_sender_text[m.sender_screen_name] = m.text + " " + unique_sender_text[m.sender_screen_name]

        for user in unique_sender_text:
            parse_text(unique_sender_text[user])
