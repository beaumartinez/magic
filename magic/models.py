from collections import namedtuple

from json import dumps

Card = namedtuple('Card', (
    'artist',
    'converted_mana',
    'flavour_text',
    'image',
    'mana',
    'name',
    'number',
    'power',
    'rarity',
    'rating',
    'set',
    'text',
    'toughness',
    'type',
    'url',
))

class Card(Card):

    def to_json(self):
        as_dict = self._asdict()
        as_dict = dict(as_dict)

        return dumps(as_dict)

Rating = namedtuple('Rating', (
    'rating',
    'vote_count',
))
