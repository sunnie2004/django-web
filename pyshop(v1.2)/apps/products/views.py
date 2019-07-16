from django.shortcuts import render,get_object_or_404
from  django.http  import HttpResponse
from .models import Product
from django.views import View
# from .forms import ProductAddToCartForm

# Create your views here.
def ProductView(request):
    products = Product.objects.all()
    # form = ProductAddToCartForm(request)   #collect all products' information
    return render(request, 'product.html', locals())



