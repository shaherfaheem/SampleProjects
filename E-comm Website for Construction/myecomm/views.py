from django.shortcuts import render,redirect
from django.http import JsonResponse
import json
import datetime
from .models import * 
from .utils import cookieCart, cartData, guestOrder
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout


def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")


def search(request):
	if request.method == "POST":
		name = request.POST['name']
		product_filter = Product.objects.filter(name__icontains=name)

		data = cartData(request)

		cartItems = data['cartItems']
		order = data['order']
		items = data['items']

		context = {'products':product_filter, 'cartItems':cartItems}
		return render(request, 'search.html', context)


def Registration(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            new_data_created = User.objects.create(
                username=username,
                email = email,
            )
            new_customer = Customer.objects.create(
                email = email,
				name = new_data_created.username,
				user_id = new_data_created.id,
                id = new_data_created.id,
			)
            new_data_created.set_password(password)
            new_customer.save
            new_data_created.save()
            return render(request, "login.html")
        else:
            return render(request, "register.html")
    return render(request, "register.html")

def LoggingIn(request):
		
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(request, username=username, password=password)
	if user is not None:
		auth_login(request, user)
		return redirect("store")
	else:
		return redirect("login")

			
def signout(request):
    logout(request)
    return render(request, "login.html")


def store(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.order_by('id')[:3]
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store.html', context)


def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'cart.html', context)

def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		

	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
			customer=customer,
			order=order,
			address=data['shipping']['address'],
			city=data['shipping']['city'],
			state=data['shipping']['state'],
			zipcode=data['shipping']['zipcode'],
			)

	return JsonResponse('Payment submitted..', safe=False)