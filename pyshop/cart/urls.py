from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.cart,name='home'),
    # path('cart_update/', views.cart_update,name='update'),
]