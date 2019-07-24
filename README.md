# django-web
History:
Version       Function     
V1.0         show product page,from the admin, edit product
v1.1         change the project structure as below:
																							apps--------
																									products--
																									cart--
																									order--
																							db---------   #for all of models
																									basemodel.py
																							media-------  #for iamge at the beginning, then changed to static/image
																							pyshop-------
																							static-------
																									 js-----
																									 css----
																									 image---  #save the image here 
																							templates-----   #include all of the templates
																							manage.py
																							db.sqlite
							cart page(including update&remove item) order page
V1.2          payment app
								pay by paypal ipn model
								paymentdone,paymentprocess,paymentcancel page
								use ngrok to test paypal signal
								add tax on the pay
  
V1.3          admin custom order view and print it by pdf
              add shipping_method,and send email to buyer

Page Layout:
		see introduction doc.
Envrionment:
		django V2.1,
		python V3.6.2,
		Pycharm community edition,
		
		cart frontend send message to backend by ajax, and save the item in session,
		order customize by inherit from admin/base_site，
	  payment api -- paypal IPN,test paypal signal by ngrok,

