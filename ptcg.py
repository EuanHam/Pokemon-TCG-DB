import info
import requests
import streamlit as st

st. set_page_config(layout="wide")

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


def main():
    st.image("banner.jpeg")
    st.title("PTCGDb ◓ : Pokémon Trading Card Game Database")
    st.write("------------------")

    # Instructions for user
    pokemon_name = st.text_input("Enter the Pokémon Card name:" + "\n" + "e.g. Try Pokémon like Garchomp or trainers like Cynthia!")
    sorting = st.selectbox(
        '',
        ('Price Descending', 'Price Ascending', 'Oldest to Newest', 'Newest to Oldest'),
        index = None,
        placeholder = "Sort By ...",
    # implement stuff from: https://docs.streamlit.io/library/api-reference/widgets/st.selectbox
    )
    costCheck = st.checkbox('Only include cards with a price')
    if st.button("Search"):
        if pokemon_name:
            pokemon_data = getInfo(pokemon_name, costCheck, sorting)
            if pokemon_data:
                st.header("Search Results")
                col1, col2, col3 = st.columns(3)

                for i in range(len(pokemon_data)):
                    if i % 3 == 0:
                        with col1:
                            st.write(pokemon_data[i][0])
                            st.image(pokemon_data[i][1], width = 200)
                    elif i % 3 == 1:
                        with col2:
                            st.write(pokemon_data[i][0])
                            st.image(pokemon_data[i][1], width = 200)
                    else:
                        with col3:
                            st.write(pokemon_data[i][0])
                            st.image(pokemon_data[i][1], width = 200)
            else:
                st.write("No data found for this Pokémon.")

if __name__ == "__main__":
    main()
def side():
    file = open("description.txt", "r")
    description = file.read()
    st.sidebar.header("About the Program")
    st.sidebar.write(description)
    st.sidebar.header("ReadMe (Not Implemented Yet)")
    linkedin_link = f'<a href="{"https://github.com/EuanHam/Pokemon-TCG-DB"}"><img src = "{info.linkedin_image_url}" alt = "LinkedIn" width = "75" height = "75"></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html = True)
    github_link = f'<a href="{info.my_github_url}"><img src = "{info.github_image_url}" alt = "GitHub" width = "75" height = "75"></a>'
    st.sidebar.markdown(github_link, unsafe_allow_html = True)
    st.sidebar.text("Email:" + "\n" + "firstLast@gmail.com")

side()
