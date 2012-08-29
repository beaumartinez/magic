#! /usr/bin/env python

from pprint import pprint
from sys import path

path.insert(0, '..')

from magic.api import get_card, get_cards, get_sets

if __name__ == '__main__':
    for set_ in get_sets():
        for page in get_cards(set_):
            for card in page:
                try:
                    card = get_card(card)
                except StandardError:
                    print card
                else:
                    pprint(card.to_dict())

                print
