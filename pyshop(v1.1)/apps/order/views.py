from django.shortcuts import render
from .models import OrderInfo, OrderProducts
from apps.products.models import Product
from django.views.generic import View
from .forms import OrderCreateForm
from django.contrib.sessions.models import Session
from .models import OrderProducts, OrderInfo

# Create your views here.
def OrderProductView(request):
    cart_products = []
    total_quantity = 0
    total_price = 0
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

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            if cart_products:
                Emptycart = False
                for item in cart_products:
                    orders = OrderProducts(orderId=order,product=item,quantity=item.quantity,price=item.price,subtotal=item.subtotal)
                    orders.save()
                    print(order.order_id)
                request.session.flush()
            # del request.session
            # if SessionBase.TEST_COOKIE_NAME not in request.session:
            #     for sesskey in request.session.keys():
            #         del request.session[sesskey]

            # request.session.clear_expired()

        return render(request,"placeorder.html",locals())

    else:
        form = OrderCreateForm()

    return render(request,"order.html",locals())
