from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from medicalCenter_app.cart import Cart
from medicalCenter_app.models import Service
from medicalCenter_app.forms import CartAddProductForm


@require_POST
def cart_add(request, service_id):
    cart = Cart(request)
    service = get_object_or_404(Service, id=service_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(service=service,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart_detail')


def cart_increment(request, service_id):
    cart = Cart(request)
    service = get_object_or_404(Service, id=service_id)
    cart.add(service)
    return redirect('cart_detail')


def cart_decrement(request, service_id):
    cart = Cart(request)
    service = get_object_or_404(Service, id=service_id)
    cart.add(service, -1)
    return redirect('cart_detail')


def cart_remove(request, service_id):
    cart = Cart(request)
    service = get_object_or_404(Service, id=service_id)
    cart.remove(service)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})