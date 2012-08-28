from collections import namedtuple

Card = namedtuple('Card', (
    'artist',
    'converted_mana',
    'flavour_text',
    'image',
    'mana',
    'name',
    'number',
    'power_toughness',
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
