from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView

from NGO_HOME.models import NGO


def ngo_home(request):
    return render(request, 'NGO_HOME/ngo_homepage.html', {'title': 'About'})


class SearchResultsView(ListView):
    model = NGO
    template_name = 'NGO_HOME/search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        query2 = self.request.GET.get('loc')
        object_list = NGO.objects.filter(
        Q(Area__icontains=query2) & Q(Domain__contains=query)
        )
        return object_list

