from django import forms
from .models import Order,OrderProducts


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'email','phone_number','addr','zip_code','city','state','shipping_method']