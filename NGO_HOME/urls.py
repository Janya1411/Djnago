from django.urls import path
from NGO_HOME import views
from NGO_HOME.views import SearchResultsView

app_name = 'ngo-home'
urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='ngo-search'),
    path('', views.ngo_home, name='ngo-home'),
]

