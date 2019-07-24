# django-web

History:
====
V1.0
----
>show product page,from the admin, edit product<br> 

V1.1
----
>change the project structure as below:  
* apps
    * product
    * cart
    * order
    * payment
* db  <!--for all of models-->
    * basemodel.py
* media  <!--for iamge at the beginning, then changed to static/image-->
* pyshop
* static			
    * js
    * css
    * image  <!--save the image here-->						
* templates   <!--include all of the templates-->							
* manage.py		
* db.sqlite
>cart page(including update&remove item) order page

V1.2 
----
>payment app
>>pay by paypal ipn model
* paymentdone,paymentprocess,paymentcancel page
* use ngrok to test paypal signal
* add tax on the pay
  
V1.3
----
* admin custom order view and print it by pdf
* add shipping_method,and shipping_fee

Page Layout:
===
![product](https://github.com/sunnie2004/django-web/blob/master/products.jpg)
![shopping-cart](https://github.com/sunnie2004/django-web/blob/master/cart.jpg)
![orderpage](https://github.com/sunnie2004/django-web/blob/master/order.jpg)
![orderadmin-change](https://github.com/sunnie2004/django-web/blob/master/orderadminchange.jpg)
![orderadmin-add action](https://github.com/sunnie2004/django-web/blob/master/orderadmin.jpg)
![orderadmin-print](https://github.com/sunnie2004/django-web/blob/master/printorder.jpg)
![ordercustomize](https://github.com/sunnie2004/django-web/blob/master/ordercustomize.png)
Envrionment:
====
| tool  | version |function|
| ------------- | ------------- |------|
| django  | V2.1  | |
| python  | V3.6.2  | |
|Pycharm | community edition| |
|paypal|ipn| for payment app|
|ngrok|V2.3.30|test paypal signal,Expose a local web server to the internet|
|github| | |

Language:
=======
* PYTHON
* HTML
* JAVASCRIPT
* CSS
* GIT
* MARKDOWN

Detail:
======
Ajax
----
>cart frontend send message to backend by ajax 

session
----
>save the item in session

customize
----------
>order customize by inherit from admin/base_site

	       
