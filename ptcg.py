import requests

def getInfo(pokemon_name, check, sortingMethod):
    base_url = "https://api.pokemontcg.io/v2/cards"
    params = {'q': f'name:"{pokemon_name}"'}

    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        data = pokemonLoop(data, check, sortingMethod)
        return data
    else:
        return "Failed to fetch data. Status code: {}".format(response.status_code)
    
def pokemonLoop(data, check, sortingMethod):
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
            if sortingMethod == "Price Ascending":
                price = 100000000000
            elif sortingMethod == "Price Descending":
                price = -1
            toAdd = "{} - {} - {} - Market Price: Not Available on TCGPlayer".format(cardName, id, set)
        if check:
            if price != 0:
                list.append((toAdd, imageURL, release, price))
        else:
            list.append((toAdd, imageURL, release, price))
    sort(list, sortingMethod)
    return list

def sort(list, sortingMethod):
    if sortingMethod == "Oldest to Newest":
        list.sort(key = lambda x: x[2])
    if sortingMethod == "Newest to Oldest":
        list.sort(key = lambda x: x[2], reverse = True)
        list.reverse()
    if sortingMethod == "Price Ascending":
        list.sort(key = lambda x: float(x[3]) if x[3] != 0 else 0)
    elif sortingMethod == "Price Descending":
        list.sort(key = lambda x: float(-1 * x[3]) if x[3] != 0 else 0)
    return list