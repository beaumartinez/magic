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

    # Handle mana
    if element.tag == 'img':
        if element.get('alt') is not None:
            formatted_element.append(element.get('alt'))

            # "Pretty print"
            if element.getnext() is not None:
                formatted_element.append(' ')

    for child in element:
        formatted_element.extend(format_paragraph(child))

    if element.tail is not None:
        formatted_element.append(element.tail)

    formatted_element = ''.join(formatted_element)

    return formatted_element
