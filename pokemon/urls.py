from django.urls import path

from pokemon.views import (HomePageView, PokemonDetailView,
                           SearchResultsListView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
    path('p/<str:name>/', PokemonDetailView.as_view(), name='pokemon_detail'),

]
