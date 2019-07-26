from django.conf import settings
from django.shortcuts import get_object_or_404
from paypal.standard.ipn.signals import valid_ipn_received
from paypal.standard.models import ST_PP_COMPLETED
from apps.order.models import Order
from django.core.mail import send_mail

# @receiver(valid_ipn_received)
def payment_notification(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        print("find it")
        # Check that the receiver email is the same we previously
        # set on the `business` field. (The user could tamper with
        # that fields on the payment form before it goes to PayPal)
        if ipn_obj.receiver_email != settings.PAYPAL_RECEIVER_EMAIL:
            # Not a valid payment
            return

        # payment was successful
        order = get_object_or_404(Order, order_id=ipn_obj.invoice)
        # mark the order as paid
        order.order_status = 2
        order.trade_no = ipn_obj.txn_id
        order.tax = ipn_obj.tax
        order.shipping_fee = ipn_obj.shipping
        print(ipn_obj.tax)
        print(ipn_obj.shipping)
        order.save()


        # send_mail('','',settings.PAYPAL_RECEIVER_EMAIL,[])
 # Retrieve the order_number previously passed
 #    order_number = ipn_obj.custom
 #    # Get the order :D
 #    order = Orders.objects.get(order_number=order_number)
# generate and send an email with pdf certificate file to the user's email
#         user_infor = ast.literal_eval(ipn_obj.custom)
#         user_info = {
#             "name": user_infor['name'],
#             "hours": user_infor['hours'],
#             "taggedArticles": user_infor['taggedArticles'],
#             "email": user_infor['email'],
#             "date": user_infor['date'],
#         }
#         html = render_to_string('users/certificate_template.html',
#                                 {'user': user_info})
#         response = HttpResponse(content_type='application/pdf')
#         response['Content-Disposition'] = 'filename=certificate_{}'.format(user_info['name']) + '.pdf'
#         pdf = weasyprint.HTML(string=html, base_url='http://8d8093d5.ngrok.io/users/process/').write_pdf(
#             stylesheets=[weasyprint.CSS(string='body { font-family: serif}')])
#         to_emails = [str(user_infor['email'])]
#         subject = "Certificate from Nami Montana"
#         email = EmailMessage(subject, body=pdf, from_email=settings.EMAIL_HOST_USER, to=to_emails)
#         email.attach("certificate_{}".format(user_infor['name']) + '.pdf', pdf, "application/pdf")
#         email.content_subtype = "pdf"  # Main content is now text/html
#         email.encoding = 'us-ascii'
#         email.send()
# def do_not_show_me_the_money(sender, **kwargs):
#     print('And Payment is not valid')
#     ipn_obj = sender
#     user_infor = ast.literal_eval(ipn_obj.custom)
#     to_emails = [str(user_infor['email'])]
#     subject = "Certificate from Nami Montana"
#     # message = 'Enjoy your certificate.'
#     email = EmailMessage(subject, body='Unfortunately, there\'s something wrong with your payment as it\'s'
#                                    'not validated.Check your PayPal account, please!',
#                      from_email=settings.EMAIL_HOST_USER, to=to_emails)
#     email.send()
valid_ipn_received.connect(payment_notification)