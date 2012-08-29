#! /usr/bin/env python

from pprint import pprint
from sys import argv, path

path.insert(0, '..')

from magic.api import get_card, get_cards, get_sets

if __name__ == '__main__':
    set_ = argv[1]

    for page in get_cards(set_):
        for card in page:
            card = get_card(card)

            pprint(card.to_dict())
            print
