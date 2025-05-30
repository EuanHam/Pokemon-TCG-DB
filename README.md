# Pokemon TCG Database

The Pokémon Trading Card Game Database or PTCGDb is a repository to search for Pokémon cards from nearly all the sets in existence. This excludes one-of-a-kind cards, instead including cards from standard sets and other promotions. 

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/EuanHam/Pokemon-TCG-DB.git
   cd Pokemon-TCG-DB
   ```
   
2. Set up a virtual environment:
   ```
   python -m venv venv_name
   source venv_name/bin/activate
   ```

3. Install dependencies:
   ```
   pip install numpy==1.24.6
   pip install streamlit
   ```
4. Start the application:
   ```
   streamlit run ptcg.py
   ```

## Usage

After starting the application, navigate to `http://localhost:3000` in your web browser. From there you can use this search tool.


## Acknowledgments

- [Pokemon TCG API](https://pokemontcg.io/) for providing card information and images
- [Pokemon Company](https://www.pokemon.com/) for creating the Pokemon Trading Card Game