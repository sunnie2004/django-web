from django.shortcuts import render, get_object_or_404,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from decimal import Decimal
from django.conf import settings
from apps.products.models import Product
from django.views import View
from django.http import JsonResponse
from django.contrib.sessions.models import Session,AbstractBaseSession

# Create your views here.
def CartAddView(request):

    if request.method == 'POST':

        item_id = request.POST.get('item_id')  # get product_name and quantity:failure
        quantity = request.POST.get('quantity')
        # print(request.POST)
        # print(request.session.session_key)

        # form = ProductAddToCartForm(request.POST)
        # if form.is_valid():
        #     quantity = form.cleaned_data["quantity"]
        #

        if not all([item_id,quantity]):    #get completed information ,{item_id:quantity}
            return JsonResponse({'res':1,'errmsg':'need more information'})
        # items = request.session.items()
        # print(items)
        # print(request.session.keys())

        if item_id not in request.session.keys():

            # print(quantity)
            # print(item_id)
            request.session[item_id] = int(quantity)
        else:
            # print(quantity)
            # print(item_id)
            request.session[item_id] = int(request.session[item_id]) + int(quantity)

        return JsonResponse({'quantity': quantity,'item_id': item_id})

def CartUpdate(request):
    if request.method == 'POST':
        update_item_id = request.POST.get('update_item_id')  # get product_name and quantity:failure
        update_quantity = request.POST.get('update_quantity')

    if update_item_id in request.session.keys():
        # print(update_item_id)
        # print(update_quantity)
        request.session[update_item_id] = int(update_quantity)
        return JsonResponse({'res':'1'})
    else:
        return JsonResponse({'res':'2'})


def CartRemove(request,id):
    if id in request.session.keys():
        del request.session[id]
    return HttpResponseRedirect("/cart")


def CartView(request):
    cart_products = []
    total_quantity = 0
    total_price = 0
    Emptycart = True

    for item, count in request.session.items():
# 7/2/2019 session middleware and class sessionstore,session,sessionbase,how they work, function decode and encode()
#use load()
        # s = Session.objects.all()   #get session
        # key = request.session.keys()
        # print(key)
        # print(s)
        #
        # sess = Session.objects.get(pk='yxifn6vx11le2c7tiexata8ectkeecs1')
        # print(sess)
        # print(sess.session_data)
        # print(sess.get_decoded())

        if item != '_auth_user_id' and item != '_auth_user_backend' and item != '_auth_user_hash':
            if not all([item,count]):
                Emptycart = True
            else:
                Emptycart = False
                # print(item)
                item = Product.objects.get(id=item)
                item.id = item.id
                item.subtotal = item.price * count
                item.price = item.price
                item.quantity = count
                cart_products.append(item)

                total_quantity += count
                total_price += item.subtotal
            # print(cart_products)
            # print(item)

    return render(request,'cart.html',locals())

