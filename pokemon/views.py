import requests
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'pokemon/home.html'


class SearchResultsListView(TemplateView):
    template_name = 'pokemon/search.html'

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('q')
        r =
        context = super().get_context_data(**kwargs)
        context['name'] = 'veer'
        return context
