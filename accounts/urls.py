from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # /accounts/
    path('', views.index, name='index'),

    # /accounts/a123/
    path('a<int:account_id>/', views.account, name='account'),

    # /accounts/a123/l123
    path('a<int:account_id>/l<int:list_id>/', views.list, name='list'),

    # /accounts/a123/lists
    path('a<int:account_id>/lists/', views.lists, name='lists'),

    # /accounts/a123/l123/i123
    path('a<int:account_id>/l<int:list_id>/i<int:item_id>/', views.item, name='item'),

    # /accounts/a123/l123/prioritized
    path('a<int:account_id>/l<int:list_id>/prioritized/', views.prioritized, name='prioritized'),
]
