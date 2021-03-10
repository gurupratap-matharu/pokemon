from django.urls import path

from pokemon.views import HomePageView

app_name = 'pokemon'

urlpatterns = [
    path('', HomePageView.as_view(), name='home')
]
