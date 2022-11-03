from django.urls import path, re_path, include
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('', views.list_providers, name = 'list_providers'),
    #---------------------BANK ACCOUNT - CONTAS BANCÁRIAS --------------------------
    path('', views.list_bank_accounts, name = 'list_bank_accounts'),
    path('', views.create_bank_account, name = 'create_bank_account'),
    path('', views.update_bank_account, name = 'update_bank_account'),
    path('', views.delete_bank_account, name = 'delete_bank_account'),

    #---------------------PROVIDER - FORNECEDORES --------------------------
    path('', views.list_providers, name = 'list_providers'),
    path('', views.create_provider, name = 'create_provider'),
    path('', views.update_provider, name = 'update_provider'),
    path('', views.delete_provider, name = 'delete_provider'),

    #---------------------CATEGORIAS                 --------------------------
    path('', views.list_categorys, name = 'list_categorys'),
    path('', views.create_category, name = 'create_category'),
    path('', views.update_category, name = 'update_category'),
    path('', views.delete_category, name = 'delete_category'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
