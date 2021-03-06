"""pyshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from apps.pages.views import home_view
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/',include('apps.products.urls'),name='product'),
    path('cart/', include('apps.cart.urls'),name='shopping cart'),
    path('order/', include('apps.order.urls'),name='order'),
    path('', home_view, name='home'),
    path('paypal/',include('paypal.standard.ipn.urls'),name='paypal'),
    path('payment/',include('apps.payment.urls'),name='payment'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
