from django.urls import path
from .views import OrderProductView


urlpatterns = [
    path('', OrderProductView, name="order"),
    # path('placeorder', views.OrderProductView,name="order"),
    # path('admin/order/<order_id>/', admin_order_detail, name='order_detail'),
]