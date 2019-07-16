from django.shortcuts import render,redirect
from .models import OrderInfo, OrderProducts
from apps.products.models import Product
from django.views.generic import View
from .forms import OrderCreateForm
from django.contrib.sessions.models import Session
from .models import OrderProducts, OrderInfo
from django.urls import reverse
from apps.payment import *
# Create your views here.
def OrderProductView(request):
    cart_products = []
    total_quantity = 0
    total_price = 0
    total_weight = 0
    Emptycart = True

    for item, count in request.session.items():
        if item != '_auth_user_id' and item != '_auth_user_backend' and  item != '_auth_user_hash':
            if not all([item,count]):
                Emptycart = True
            else:
                Emptycart = False
                item = Product.objects.get(id=item)
                item.id = item.id
                item.subtotal = item.price * count
                item.price = item.price
                item.quantity = count
                cart_products.append(item)

                total_quantity += count
                total_price += item.subtotal
                total_weight += item.weight * item.quantity

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            print("order_id is {}".format(order.order_id))
            order.total_quantity = total_quantity
            order.total_price = total_price
            if cart_products:
                Emptycart = False
                for item in cart_products:
                    orders = OrderProducts(orderId=order,product=item,quantity=item.quantity,price=item.price,subtotal=item.subtotal)
                    orders.save()
                print("order id is {}".format(order))

                order.save()
                # request.session.flush()
            # del request.session
            # if SessionBase.TEST_COOKIE_NAME not in request.session:
            #     for sesskey in request.session.keys():
            #         del request.session[sesskey]

            # request.session.clear_expired()
        return redirect(reverse('payment:process',kwargs={'order_id':order.order_id}))  #reverse to pass parameter order_id 7/10/2019

        # return render(request,"placeorder.html",locals())

    else:
        form = OrderCreateForm()

    return render(request,"order.html",locals())

#
# def admin_order_detail(request, order_id):
#     order = get_object_or_404(OrderInfo, id=order_id)
#     return render(request, 'admin/order/orderinfo/detail.html', {'order': order})