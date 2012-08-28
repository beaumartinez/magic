from itertools import imap
from re import findall

def coerce_mana(mana):
    try:
        mana = int(mana)
    except ValueError:
        mana = mana.lower()

    return mana

def format_paragraph(element):
    formatted_element = list()

    if element.text is not None:
        formatted_element.append(element.text)

    # Handle images
    if element.tag == 'img':
        if element.get('alt') is not None:
            formatted_element.append('({})'.format(element.get('alt')))

            # "Pretty print"
            if element.getnext() is not None:
                if element.tail is None:
                    formatted_element.append(' ')

    for child in element:
        formatted_element.extend(format_paragraph(child))

    if element.tail is not None:
        formatted_element.append(element.tail)

    formatted_element = ''.join(formatted_element)

    return formatted_element

def split_power_toughness(power_toughness):
    power, toughness = findall('(\d+)', power_toughness)
    power, toughness = imap(int, (power, toughness))

    return power, toughness
