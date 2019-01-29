from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .cart import Cart
from shop.models import Product

# Create your views here.

@require_POST
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product)
    print(cart)
    return redirect('cart:cart_details')

@require_POST
def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_details')

@require_POST
def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart:cart_details')

def cart_details(request):
    cart = Cart(request)
    context = {'cart': cart}
    return render(request, 'cart/cart_details.html', context)
