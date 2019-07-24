from django.apps import AppConfig


class PaymentConfig(AppConfig):
    name = 'apps.payment'
    verbose_name = 'Payment'

    def ready(self):
        import apps.payment.signals     # import signal handlers