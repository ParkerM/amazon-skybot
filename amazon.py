import re
from amazonproduct import API
from util import hook, http

amazon_re = (r'amazon.com\/.*dp\/[A-Z0-9]*', re.I)

@hook.regex(*amazon_re)
def amazon_url(match, say=None):
    url = match.group(0)
    index = url.find('dp/', 0)
    id = url[index+3:]

    api = API(locale='us')
    result = api.item_lookup(id)

    for item in result.Items.Item:
        description = item.ItemAttributes.Title + " - "

    price = api.item_lookup(id, ResponseGroup='Offers')

    for a in price.Items.Item.Offers.Offer:
        description += a.OfferListing.Price.FormattedPrice

    say(description)
