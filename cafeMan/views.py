from django.shortcuts import render, HttpResponse
from .models import Dish, Orders
import json
from . import ml
import math, random
from django.template.loader import get_template
import pdfkit

# Create your views here.
def location(request):
    # dish = Dish(name="vadapav", price=10, etp=2, special_day="Mon")
    return render(request, "hello/location.html")

def product(request):
	return render(request, "hello/categories.html")

def order(request, food_id):
	image_data = ['sand.jpeg', 'dosa.jpeg', 'noodles.jpeg']
	dish_values = [60, 20, 80]
	context = {
		"image_name" : image_data[food_id - 1],
		"value" : dish_values[food_id - 1]
	}

	return render(request, "hello/order.html", context)

def cart(request):
	return render(request, 'hello/cart.html')

def checkout(request):
	username = request.user.username
	orders = Orders.objects.filter(order_active=True).all()
	context = {
		"items_ordered" : set(),
		"total" : 0,
		"recommended" : None
	}
	
	for order in orders:
		for dish in order.order_items.all():
			context["items_ordered"].add(dish)
			context["total"] += dish.price * dish.quantity
	

	context["items_ordered"] = list(context["items_ordered"])
	if context["items_ordered"][0] == "dosa":
		context["recommended"] = ml.dosarec()
	elif context["items_ordered"][0] == "noodles":
		context["recommended"] = ml.noodrec()
	else:
		context["recommended"] = ml.sandrec()
	 
	return render(request, 'hello/checkout.html', context)

def contact(request):
	return render(request, 'hello/contact.html')

def add_item_to_order(request):
	if request.method == 'POST' and request.is_ajax():
		print("Ajax call started !!!")

		item_nam = request.POST['dish_name']
		
		item_name = item_nam.replace('.jpeg', '')

		item_quantity = request.POST['dish_quantity']

		# order_by_user = Orders.objects.get(placed_by=request.user)
		dishes = {
			"dosa" : ["dosa", 20, 10, 'MON'],
			"sand" : ["sandwich", 60, 20, "WED"],
			"noodles" : ["noodles", 80, 15, "SAT"]
		}

		l = dishes[item_name]
		new_dish = Dish(name=l[0],price = l[1], etp = l[2], special_day=l[3], quantity=item_quantity)
		new_dish.save()

		new_order = Orders(placed_by=request.user)
		new_order.save()
		new_order.order_items.add(new_dish)


		# if order_by_user : 
		# 	new_dish = Dish(name=item_name,price = 100, etp = 15, special_day='Mon', quantity=item_quantity, rating=4)

		# 	new_dish.save()

		# 	order_by_user.order_items.add(new_dish)

		# else :
		# 	new_dish = Dish(name=item_name,price = 100, etp = 15, special_day='Mon', quantity=item_quantity, rating=4)

		# 	new_dish.save()

		# 	new_order = Order(placed_by=request.user)

		# 	new_order.save()

		# 	new_order.order_items(new_dish)

	return HttpResponse("OK")


def admin_dashboard(request):

    context = {"predictions" : {"sandwich" : ml.sandpred(), "noodels" : ml.noodpred(), "dosa" : ml.dosapred()}}
    return render(request, "hello/admin_dash.html", context)

def otp(request):
	username = request.user.username
	orders = Orders.objects.filter(order_active=True).all()
	otp = generateOTP() + username
	for order in orders:
		order.otp=otp
		order.save()


	return render(request, "hello/otp.html", {"otp" : otp})

def generateOTP() :   
    digits = "0123456789"
    OTP = ""  
    for i in range(4) : 
        OTP += digits[math.floor(random.random() * 10)] 
  
    return OTP 

def send_pdf(request):
	username = request.user.username
	orders = Orders.objects.filter(order_active=True).all()
	context = {
		"user" : username,
		"items_ordered" : set(),
		"total" : 0
	}
	
	for order in orders:
		for dish in order.order_items.all():
			context["items_ordered"].add(dish)
			context["total"] += dish.price * dish.quantity
	
	context["items_ordered"] = list(context["items_ordered"])
	
	

	template = get_template('hello/test.html')
	html = template.render(context)
	pdf = pdfkit.from_string(html, False)
	response = HttpResponse(pdf, content_type = "application/pdf")
	response['Content-Disposition']  = 'attachment'; filename = "bill.pdf"

	return response

def otpVerify(request):
	username = request.user.username
	if request.method == 'POST' and request.is_ajax():
		
		orders = Orders.objects.filter(order_active=True).all()
		otp = request.POST["otp"]
		print(otp)
		for order in orders:
			print(otp, order.otp)
			if order.otp == otp:
				order.order_active=False
				order.save()
	return HttpResponse("OK")
	