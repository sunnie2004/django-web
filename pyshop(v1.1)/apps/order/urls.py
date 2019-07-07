from django.urls import path
from . import views


urlpatterns = [
    path('', views.OrderProductView,name="order"),
    # path('placeorder', views.OrderProductView,name="order"),
]