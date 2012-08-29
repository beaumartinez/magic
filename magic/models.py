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

    def to_dict(self):
        as_dict = self._asdict()
        as_dict = dict(as_dict)

        return as_dict

    def to_json(self):
        as_dict = self.to_dict()
        as_json = dumps(as_dict)

        return as_json

Rating = namedtuple('Rating', (
    'rating',
    'vote_count',
))
