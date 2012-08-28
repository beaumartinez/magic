from itertools import ifilter, imap
from urlparse import urljoin

from magic.models import Rating
from magic.utils import coerce_mana, format_paragraph

# Cards

def parse_name(tree):
    name = tree.cssselect('#ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_nameRow .value')
    name = name[0]
    name = name.text
    name = name.strip()

    return name

def parse_mana(tree):
    mana = tree.cssselect('#ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_manaRow .value img')
    mana = (mana.get('alt') for mana in mana)
    mana = imap(coerce_mana, mana)

    return mana

def parse_converted_mana(tree):
    converted_mana = tree.cssselect('#ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_cmcRow .value')
    converted_mana = converted_mana[0]
    converted_mana = converted_mana.text
    converted_mana = converted_mana.strip()
    converted_mana = int(converted_mana)

    return converted_mana

def parse_type(tree):
    type_ = tree.cssselect('#ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_typeRow .value')
    type_ = type_[0]
    type_ = type_.text
    type_ = type_.strip()

    return type_

def parse_text(tree):
    text = tree.cssselect('#ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_textRow .cardtextbox')
    text = imap(format_paragraph, text)
    text = '\n'.join(text)

    return text

def parse_flavour_text(tree):
    flavour_text = tree.cssselect('#ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_FlavorText .cardtextbox')
    flavour_text = imap(format_paragraph, flavour_text)
    flavour_text = '\n'.join(flavour_text)

    if flavour_text == '':
        flavour_text = None

    return flavour_text

def parse_attack_defence(tree):
    attack_defence = tree.cssselect('#ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ptRow .value')

    try:
        attack_defence = attack_defence[0]
    except IndexError:
        attack_defence = None
    else:
        attack_defence = attack_defence.text
        attack_defence = attack_defence.strip()

    return attack_defence

def parse_set(tree):
    set_ = tree.cssselect('#ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_currentSetSymbol a')
    set_ = set_[1]
    set_ = set_.text

    return set_

def parse_rarity(tree):
    rarity = tree.cssselect('#ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_rarityRow .value span')
    rarity = rarity[0]
    rarity = rarity.text
    rarity = rarity.strip()
    rarity = rarity.lower()

    return rarity

def parse_number(tree):
    number = tree.cssselect('#ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_numberRow .value')
    number = number[0]
    number = number.text
    number = number.strip()
    number = int(number)

    return number

def parse_artist(tree):
    artist = tree.cssselect('#ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ArtistCredit a')
    artist = artist[0]
    artist = artist.text

    return artist

def parse_rating(tree):
    rating = tree.cssselect('.textRatingValue')
    rating = rating[0]
    rating = rating.text
    rating = float(rating)

    vote_count = tree.cssselect('.totalVotesValue')
    vote_count = vote_count[0]
    vote_count = vote_count.text
    vote_count = int(vote_count)

    rating = Rating(rating=rating, vote_count=vote_count)

    return rating

def parse_image(tree, url):
    image = tree.cssselect('#ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_cardImage')
    image = image[0]
    image = image.get('src')
    image = urljoin(url, image)

    return image

# Other

def parse_sets(tree):
    sets = tree.cssselect('#ctl00_ctl00_MainContent_Content_SearchControls_setAddText option')
    sets = (set_.text for set_ in sets)
    sets = ifilter(None, sets)

    return sets

def parse_links(tree, url):
    links = tree.cssselect('.cardTitle a')
    links = (link.get('href') for link in links)
    links = (urljoin(url, link) for link in links)

    return links

def parse_next_link(tree, url):
    next_link = tree.xpath(u'//a[text()="\xa0>"]')

    try:
        next_link = next_link[0]
    except IndexError:
        next_link = None
    else:
        next_link = next_link.get('href')
        next_link = urljoin(url, next_link)

    return next_link
