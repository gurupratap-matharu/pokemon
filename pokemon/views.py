from django.views.generic import TemplateView

from pokemon.api import PokemonAPI

API = PokemonAPI()
API.fetch_pokemon_list()


class HomePageView(TemplateView):
    template_name = 'pokemon/home.html'


class SearchResultsListView(TemplateView):
    template_name = 'pokemon/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pokemon_list'] = API.get_pokemons(self.request.GET.get('q'))
        return context


class PokemonDetailView(TemplateView):
    template_name = 'pokemon/pokemon_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pokemon'] = API.get_pokemon_by_name(kwargs.get('name'))

        return context
