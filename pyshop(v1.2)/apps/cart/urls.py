from django.urls import path
from . import views

urlpatterns = [
    path('', views.CartView, name='cart'),
    path('add', views.CartAddView, name='add'),
    path('remove/<id>', views.CartRemove, name='remove'),
    path('update', views.CartUpdate, name='update'),
    # url(r'add/(?P<item_name>)', views.CartAddView)
]