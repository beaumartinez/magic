from collections import namedtuple

Card = namedtuple('Card', (
    'artist',
    'attack_defence',
    'converted_mana',
    'flavour_text',
    'image',
    'mana',
    'name',
    'number',
    'rarity',
    'rating',
    'set',
    'text',
    'type',
    'url',
))

Rating = namedtuple('Rating', (
    'rating',
    'vote_count',
))
