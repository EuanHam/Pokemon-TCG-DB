# to do - have default image for pokemon card if the back if just showing because it's too big rn
# sort by price ascending and descending
# check rubric for other user input
# write description and info for side bar

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
import info
import streamlit as st
import ptcg

st. set_page_config(layout="wide")

def main():
    st.image("banner.jpeg")
    st.title("PTCGDb ◓ : Pokémon Trading Card Game Database")
    st.write("------------------")

    # Instructions for user
    # new
    pokemon_name = st.text_input("Enter the Pokémon Card name:" + "\n" + "e.g. Try Pokémon like Garchomp or trainers like Cynthia!")
    # new
    sorting = st.selectbox(
        'Label',
        ('Price Descending', 'Price Ascending', 'Oldest to Newest', 'Newest to Oldest'),
        index = None,
        label_visibility="hidden",
        placeholder = "Sort By ...",
    # implement stuff from: https://docs.streamlit.io/library/api-reference/widgets/st.selectbox
    )
    # new
    costCheck = st.checkbox('Only include cards with a price')
    enterDetection = st.text_input("\n")
    # new
    # new
    if st.button("Search") or enterDetection:
        if pokemon_name:
            # gets that
            pokemon_data = ptcg.getInfo(pokemon_name, costCheck, sorting)

            if pokemon_data:
                # shows data
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
# Ripped this part from the tutorial
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