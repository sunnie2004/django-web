# from  django import forms
# from .models import Product
#
# class ProductAddToCartForm(forms.Form):
#     quantity = forms.IntegerField(label='quantity',
#                                   widget=forms.TextInput(
#                                       attrs={
#                                           'size': '2',
#                                           'value': '0',
#                                           'class': 'quantity',
#                                           'max_length': '5',
#                                       }),
#                                   error_messages={'invalid': 'please input valid number!'},
#                                   min_value=1,
#                                   max_value=Product.stock,
#                                   )
#     product_slug = forms.CharField(widget=forms.HiddenInput())
#
#     def __init__(self, request=None, *args, **kwargs):
#         self.request = request
#         super(ProductAddToCartForm, self).__init__(*args, **kwargs)
