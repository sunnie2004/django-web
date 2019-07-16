from django import forms
from .models import OrderInfo,OrderProducts


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = OrderInfo
        fields = ['user', 'email','phone_number','addr','zip_code','city','state']