from collections import namedtuple

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

Rating = namedtuple('Rating', (
    'rating',
    'vote_count',
))
