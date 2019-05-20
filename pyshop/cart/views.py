from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Cart

# Create your views here.
def cart(request):
    # cart_id = request.session.get("card_id",None)
    # qs = Cart.objects.filter(id=cart_id)
    # if qs.count() == 1:
    #     cart_obj = qs.first()
    #     if request.user.is_authenticated() and cart_obj.user is None:
    #         cart_obj.user= request.user
    #         cart_obj.save()
    # else:
    #     cart_obj = Cart.objects.new(user=request.user)
    #     request.session['cart_id'] = cart_obj.id
    #
    # products = cart_obj.products.all()
    #
    # total = 0
    # for x in products:
    #     total += x.price
    # cart_obj.total = total
    # cart_obj.save()
    return render(request,'cart.html',{})


# def cart_update(request):
#     product_obj = Product.objects.get()
#     cart_obj, new_obj = Cart.objects.new_or_get(request)
#     if product_obj in cart_obj.products.all():
#         cart_obj.products.remove(product_obj)
#     else:
#         cart_obj.products.add(product_obj)
#
#     return redirect("cart")