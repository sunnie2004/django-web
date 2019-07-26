from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from apps.order.models import Order
from django.conf import settings
from decimal import Decimal
# Create your views here.

def payment_process(request,order_id):

    try:
        order = Order.objects.get(order_id=order_id)
    except:
        # messages.add_message(request, messages.WARNING, "wrong order serial number!")
        return redirect('/order')
    # print(order.order_id)
    # order = get_object_or_404(OrderInfo, id=order_id)
    host = request.get_host()
    # What you want the button to do.
    # all_order_items = models.OrderItem.objects.filter(order=order)
    # items = list()
    # total = 0
    # for order_item in all_order_items:
    #     t = dict()
    #     t['name'] = order_item.product.name
    #     t['price'] = order_item.product.price
    #     t['quantity'] = order_item.quantity
    #     t['subtotal'] = order_item.product.price * order_item.quantity
    #     total = total + order_item.product.price
    #     items.append(t)
    if order.shipping_method == 1:
        if order.total_weight <= 16:
            order.shipping_fee = Decimal(0.1)
        else:
            order.shipping_fee = Decimal(0.2)
    else:
        if order.total_weight <= 16:
            order.shipping_fee = Decimal(0.2)
        else:
            order.shipping_fee = Decimal(0.4)

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '%.2f' % (order.total_price),
        'item_name': 'WAXBEE CANDLES',
        'invoice': str(order.order_id),
        # 'invoice':"unique-invoice-id",
        'address_street':order.addr,
        'shipping_method': order.shipping_method,
        'shipping': order.shipping_fee,
        'address_zip': order.zip_code,
        'address_city': order.city,
        'address_state': order.state,
        'address_country': 'USA',
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host,reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment:done',kwargs={'order_id':order.order_id})),
        'cancel_return': 'http://{}{}'.format(host,reverse('payment:canceled')),
    }
    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, "payment.html", context)

@csrf_exempt
def payment_done(request,order_id):
    try:
        order = Order.objects.get(order_id=order_id)
    except:
        return

    request.session.flush()
    return render(request, 'paymentdone.html',locals())


@csrf_exempt
def payment_canceled(request):
    return render(request, 'paymentcancel.html')