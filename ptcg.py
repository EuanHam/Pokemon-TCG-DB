import info
import requests
import streamlit as st


def getInfo(pokemon_name, check, sorting):
    base_url = "https://api.pokemontcg.io/v2/cards"
    # Creates parameters for the API request sourced from w3schools
    params = {'q': f'name:"{pokemon_name}"'}

    # Make the get request to the API
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        # get json data if there aren't any complications
        data = response.json()
        data = pokemonLoop(data, check, sorting)
        return data
    else:
        # else, fail message
        return "Failed to fetch data. Status code: {}".format(response.status_code)
    
def pokemonLoop(data, check, sorting):
    list = []
    toAdd = ""
    infoList = data["data"]
    for item in infoList:
        toAdd = ""
        cardName = item["name"]
        set = item["set"]["name"]
        id = item["id"]
        release = item["set"]["releaseDate"]
        try:
            imageURL = item["images"]["small"]
        except:
            imageURL = item["images"]["big"]
        toAdd = ""
        normalPrice = 0
        holofoilPrice = 0
        price = 0
        try:
            normalPrice = float(item["tcgplayer"]["prices"]["normal"]["market"])
        except:
            normalPrice = 0

        try:
            holofoilPrice = float(item["tcgplayer"]["prices"]["holofoil"]["market"])
        except:
            holofoilPrice = 0
        if normalPrice != 0:
            price = normalPrice
            toAdd = "{} - {} - {} - Market Price: ${}".format(cardName, id, set, normalPrice)
        elif holofoilPrice != 0:
            price = holofoilPrice
            toAdd = "{} - {} - {} - Market Holofoil Price: ${}".format(cardName, id, set, holofoilPrice)
        else:
            if sorting == "Price Ascending":
                price = 100000000000
            elif sorting == "Price Descending":
                price = -1
            toAdd = "{} - {} - {} - Market Price: Not Available on TCGPlayer".format(cardName, id, set)
        if check:
            if price != 0:
                list.append((toAdd, imageURL, release, price))
        else:
            list.append((toAdd, imageURL, release, price))
    if sorting == "Oldest to Newest":
        list.sort(key = lambda x: x[2])
    if sorting == "Newest to Oldest":
        list.sort(key = lambda x: x[2])
        list.reverse()
    if sorting == "Price Ascending":
        list.sort(key = lambda x: float(x[3]) if x[3] != 0 else 0)
    elif sorting == "Price Descending":
        list.sort(key = lambda x: float(-1 * x[3]) if x[3] != 0 else 0)
    return list
