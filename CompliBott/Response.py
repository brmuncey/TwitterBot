import random

import enchant


class Response(object):
    text = ""
    response = ""
    dict = enchant.Dict("en_US")

    def __init__(self, text):
        print("Building Response")
        self.text = text.split()
        self.__build_response__()

    def __build_response__(self):
        for text in self.text:
            self.__read_text__(text)

    def __read_text__(self, text):
        if self.__is_word__(text):
            print("Valid Word")
        else:
            print("Invalid Word")

    def __is_word__(self, text):
        return self.dict.check(text)

    def __get_rand__(self, table):
        return random.randint(1, len(self.db.child(table).get().val()))
