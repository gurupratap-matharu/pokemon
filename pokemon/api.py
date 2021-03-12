import requests
from django.conf import settings


class PokemonAPI:
    """
    API controller class to fetch data from pokeapi.co
    """

    def __init__(self):
        self.pokemons = []

    def get_pokemons(self, name=None):
        """
        Higher level method to fetch pokemon by the exact name
        or partially matching names.
        """
        return self.search_pokemon_by_partial_name(name)

    def fetch_pokemon_list(self):
        """
        Fetches a list of all available pokemons on PokeAPI.
        """
        url = settings.POKEMON_BASE_URL + '?limit=1118'
        response = requests.get(url)
        self.pokemons = response.json()['results']

    def get_pokemon_by_id(self, id=None):
        """
        Fetches all the data of a pokemon by its unique id.
        """
        pass

    def get_pokemon_by_name(self, name=None):
        """
        Fetches all the data of a pokemon by its unique name.
        """

        url = "{}{}/".format(settings.POKEMON_BASE_URL, name)
        response = requests.get(url)

        if response.ok:
            return response.json()
        return {}

    def search_pokemon_by_partial_name(self, name=None):
        """
        Returns a list of all availabe pokemons with names 
        partially matching to query.
        """

        return [p for p in self.pokemons if name in p['name']]
