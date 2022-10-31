from django.urls import path, re_path, include
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('', views.list_providers, name = 'list_providers'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
