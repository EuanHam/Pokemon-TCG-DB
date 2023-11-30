# http status codes
"""
200 - OK
400 - Bad Request (Incorrect query string parameter)
402 - Request Fail (valid, but request failed)
403 - Forbidden (user doesn't have permissions)
404 - Not Found - Requested resource doesn't exist
429 - Too Many Requests - The rate limit has been exceeded
500, 502, 503, 504 - Server Errors (Not client-side)
"""
import requests
import streamlit as st

def get_pokemon_info(pokemon_name):
    base_url = "https://api.pokemontcg.io/v2/cards"
    # Creates parameters for the API request
    params = {'q': f'name:"{pokemon_name}"'}

    # Make the get request to the API
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        # get json data if there aren't any complications
        data = response.json()
        data = pokemonLoop(data)
        return data
    else:
        # else, fail message
        return "Failed to fetch data. Status code: {}".format(response.status_code)
    
def pokemonLoop(data):
    list = []
    toAdd = ""
    infoList = data["data"]
    for item in infoList:
        cardName = item["name"]
        set = item["set"]["name"]
        id = item["id"]
        toAdd = ""
        normalPrice = 0
        holofoilPrice = 0
        try:
            normalPrice = str(item["tcgplayer"]["prices"]["normal"]["market"])
        except:
            normalPrice = 0

        try:
            holofoilPrice = str(item["tcgplayer"]["prices"]["holofoil"]["market"])
        except:
            holofoilPrice = 0
        if normalPrice != 0:
            toAdd = "{} - {} - {} - Market Price: ${}".format(cardName, id, set, normalPrice)
        elif holofoilPrice != 0:
            toAdd = "{} - {} - {} - Market Holofoil Price: ${}".format(cardName, id, set, holofoilPrice)
        else:
            toAdd = "{} - {} - {} - Market Price: Not Available on TCGPlayer".format(cardName, id, set)
        list.append(toAdd)
    return list


def main():
    st.image("banner.jpeg")
    st.title("PTCGDb ◓ : Pokémon Trading Card Game Database")
    st.write("------------------")

    # Instructions for user
    pokemon_name = st.text_input("Enter the Pokémon Card name:" + "\n" + "e.g. Try Pokémon like Garchomp or trainers like Cynthia!")

    if st.button("Search"):
        if pokemon_name:
            # gets that
            pokemon_data = get_pokemon_info(pokemon_name)

            if pokemon_data:
                # shows data
                st.header("Search Results")

                for card_info in pokemon_data:
                    st.write(card_info)
            else:
                st.write("No data found for this Pokémon.")

if __name__ == "__main__":
    main()
