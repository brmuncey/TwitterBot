import json

import warlock

schema = {
    'name': 'MENTION',
    'type': 'object',
    'properties': {
        'id': {'type': 'integer'},
        'screen_name': {'type': 'string'},
        'text': {'type': 'string'},
    },
    'additionalProperties': False,
}

MENTION = warlock.model_factory(schema)


class Mention(object):
    id = ""
    screen_name = ""
    text = ""

    def __init__(self, json_str):
        json_obj = json.loads(str(json_str))
        print(json_str)
        mention = MENTION(id=json_obj["id"], screen_name=json_obj["user"]["screen_name"], text=json_obj["text"])
        self.id = mention.id
        self.screen_name = mention.screen_name
        self.text = mention.text
