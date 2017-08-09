import json

import warlock

schema = {
    'name': 'DirectMessage',
    'type': 'object',
    'properties': {
        'id': {'type': 'integer'},
        'created_at': {'type': 'string'},
        'sender_id': {'type': 'integer'},
        'text': {'type': 'string'},
    },
    'additionalProperties': False,
}

DirectMessage = warlock.model_factory(schema)


class Message(object):
    message = ""

    def __init__(self, jsonStr):
        jsonOBJ = json.loads(jsonStr)
        self.message = DirectMessage(id=jsonOBJ["id"],
                                     created_at=jsonOBJ["created_at"],
                                     sender_id=jsonOBJ["sender_id"],
                                     text=jsonOBJ["text"])

    def get_message(self):
        return self.message
