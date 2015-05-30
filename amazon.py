import re
from amazonproduct import API
from util import hook, http

@hook.command
def amazon(inp, say=None):
    '.amazon <query> -- returns the first Amazon search result for <query>'

    api = API(locale='us')
    result = api.item_lookup(inp)

    for item in result.Items.Item:
        description = item.ItemAttributes.Title + " - "

    price = api.item_lookup(inp, ResponseGroup='Offers')

    for a in price.Items.Item.Offers.Offer:
        description += a.OfferListing.Price.FormattedPrice

    say(description)
