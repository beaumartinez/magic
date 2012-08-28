from json import dumps

from lxml.html import fromstring
from requests import get

from magic import parser
from magic.constants import SEARCH_URL_TEMPLATE, SET_LIST_URL
from magic.models import Card

def get_sets():
    document = get(SET_LIST_URL)
    tree = fromstring(document.content)

    sets = parser.parse_sets(tree)

    return sets

def get_cards(set_):
    url = SEARCH_URL_TEMPLATE.format(set_)

    while url is not None:
        document = get(url)
        tree = fromstring(document.content)

        links = parser.parse_links(tree, url)
        next_link = parser.parse_next_link(tree, url)

        url = next_link

        yield links

def get_card(url):
    document = get(url)
    tree = fromstring(document.content)

    name = parser.parse_name(tree)
    mana = parser.parse_mana(tree)
    converted_mana = parser.parse_converted_mana(tree)
    type_ = parser.parse_type(tree)
    text = parser.parse_text(tree)
    flavour_text = parser.parse_flavour_text(tree)
    power, toughness = parser.parse_power_toughness(tree)
    set_ = parser.parse_set(tree)
    rarity = parser.parse_rarity(tree)
    number = parser.parse_number(tree)
    artist = parser.parse_artist(tree)
    rating = parser.parse_rating(tree)
    image = parser.parse_image(tree, url)

    return Card(artist=artist, converted_mana=converted_mana, image=image, flavour_text=flavour_text, mana=mana, name=name, number=number, power=power, rarity=rarity, rating=rating, set=set_, text=text, toughness=toughness, type=type_, url=url)

def card_to_json(card):
    card = card._asdict()
    card = dict(card)

    return dumps(card)
