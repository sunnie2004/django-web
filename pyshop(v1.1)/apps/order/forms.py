from django import forms
from .models import OrderInfo,OrderProducts


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = OrderInfo
        fields = ['user', 'email', 'addr', 'zip_code', 'city','state',]