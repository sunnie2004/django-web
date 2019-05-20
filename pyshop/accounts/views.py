from django.shortcuts import render
from .models import Profile

# Create your views here.
def my_profile(request):
    my_user_profile = Profile.objects.filter(user=request.user).first()
    my_order = Order.objects.filter(is_ordered=True,owner=my_user_profile)

    context ={
        'my_orders':my_order
    }

    return render(request,'profile.html',context)