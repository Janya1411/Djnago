from django.urls import path, re_path
from django.conf.urls import url
from . import views
from social.views import room_detail,token

app_name = 'social'
urlpatterns = [
    re_path(r'^$', views.room_detail, name='room_detail'),
    re_path(r'^token', views.token, name='token'),

]

