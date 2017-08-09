class Response(object):
    text = ""
    response = ""

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
            #No typos reply respond with a compliment
        else:
            print("Invalid Word")
            #Acknowledge typo in message.

    def __is_word__(self, text):
        #todo check dictionary for word occurance
        return False
