from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order
from .forms import ProductForm, NewUserForm, OrderForm 
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.utils import timezone

# Terméklista
def product_list(request):
    products = Product.objects.order_by('price')
    return render(request, 'shop/product_list.html', {'products': products})

# Egy termék adatai
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})

# Új termék létrehozása
def product_new(request):
    if request.method == "POST":
        form = ProductForm(request.POST, files=request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'shop/product_edit.html', {'form': form})

# Termék szerkesztése
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)

    # Törlés
    if request.method == 'POST' and 'delete' in request.POST:
        Product.objects.filter(pk=product.pk).delete()
        return redirect('product_list') 

    # Mentés
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product, files=request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'shop/product_edit.html', {'form': form})

# Regisztrálás
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Sikeres regisztráció." )
			return redirect('product_list')
		messages.error(request, "Sikertelen regisztráció")
	form = NewUserForm()
	return render (request=request, template_name="shop/register.html", context={"register_form":form})

# Bejelentkezés
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"Bejelentkeztél {username} néven.")
				return redirect("product_list")
			else:
				messages.error(request,"Hibás felhasználónév vagy jelszó.")
		else:
			messages.error(request,"Hibás felhasználónév vagy jelszó.")
	form = AuthenticationForm()
	return render(request=request, template_name="shop/login.html", context={"login_form":form})

# Kijelentkezés
def logout_request(request):
	logout(request)
	messages.info(request, "Sikeres kijelentkezés.") 
	return redirect("product_list")

# Rendelés
def make_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user_name = request.user
            order.order_time = timezone.now()
            order.save()
            return redirect('order_complete')
    else:
        form = OrderForm()
    return render(request, 'shop/make_order.html', {'form': form})

def order_complete(request):
    return render(request, 'shop/order_complete.html', {})

# Rendelések listája:
def order_list(request):
    orders = Order.objects.order_by('order_time')
    return render(request, 'shop/order_list.html', {'orders': orders})

# Egy rendelés részletesen
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'shop/order_detail.html', {'order': order})

# Rendelés szerkesztése
def order_edit(request, pk):
    order = get_object_or_404(Order, pk=pk)

    # Törlés
    if request.method == 'POST' and 'delete' in request.POST:
        Order.objects.filter(pk=order.pk).delete()
        return redirect('order_list') 

    # Mentés
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            return redirect('order_detail', pk=order.pk)
    else:
        form = OrderForm(instance=order)
    return render(request, 'shop/make_order.html', {'form': form})
