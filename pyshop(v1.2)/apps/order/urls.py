from django.urls import path
from . import views


urlpatterns = [
    path('', views.OrderProductView, name="order"),
    # path('placeorder', views.OrderProductView,name="order"),
    # path('admin/order/(?P<order_id>\d+)/$', views.admin_order_detail, name='admin_order_detail'),
]