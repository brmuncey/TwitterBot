import json

import warlock

schema = {
    'name': 'DirectMessage',
    'type': 'object',
    'properties': {
        'id': {'type': 'integer'},
        'created_at': {'type': 'string'},
        'sender_screen_name': {'type': 'string'},
        'text': {'type': 'string'},
    },
    'additionalProperties': False,
}

DirectMessage = warlock.model_factory(schema)


class Message(object):
    message = ""

    def __init__(self, json_str):
        json_obj = json.loads(json_str)
        self.message = DirectMessage(id=json_obj["id"],
                                     created_at=json_obj["created_at"],
                                     sender_screen_name=json_obj["sender_screen_name"],
                                     text=json_obj["text"])

    def get_message(self):
        return self.message
