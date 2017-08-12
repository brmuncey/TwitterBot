import random


def __case_letter__(text):
    new_text = ""
    for letter in text:
        num = random.randint(1, 100)
        if num > 45:
            new_text += letter.upper()
        else:
            new_text += letter
    return new_text


def __modify_text__(text):
    if text == "@mockbott":
        return ""
    else:
        return __case_letter__(text) + " "


class Response(object):
    mention = ""
    response = ""

    def __init__(self, mention):
        print("Building Response")
        self.mention = mention
        self.__build_response__()
        self.__check_character_count()

    def __build_response__(self):
        words = self.mention.text.lower().split()
        for text in words:
            self.response += __modify_text__(text)
        self.response = "@" + __case_letter__(self.mention.screen_name) + " " + self.response

    def __check_character_count(self):
        total = len(self.response)
        if total <= 139:
            self.response = self.response[:-1]
            self.response += " 😂"
        else:
            difference = 140 - total
            self.response = self.response[:difference]
