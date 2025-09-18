from django.shortcuts import render, get_object_or_404, redirect
from movies.models import Movie
from .utils import calculate_cart_total
from .models import Order, Item
from django.contrib.auth.decorators import login_required

def index(request):
    template_data = {'title': 'Cart'}

    for i in range(1, 4):
        cart_key = f'cart{i}'
        cart = request.session.get(cart_key, {})
        movie_ids = list(cart.keys())
        movies_in_cart = Movie.objects.filter(id__in=movie_ids) if movie_ids else []
        cart_total = calculate_cart_total(cart, movies_in_cart) if movie_ids else 0
        template_data[f'cart{i}_movies'] = movies_in_cart
        template_data[f'cart{i}_total'] = cart_total

    return render(request, 'cart/index.html', {'template_data': template_data})


def add(request, id, cartNum=0):
    """
    Add a movie to the selected cart (1, 2, or 3).
    """
    if request.method == "POST":
        movie = get_object_or_404(Movie, id=id)

        # Read cart number from POST if available, else use URL
        cartNum = int(request.POST.get('cart_choice', cartNum))
        cart_key = f'cart{cartNum}'

        # Get or create cart
        cart = request.session.get(cart_key, {})

        # Get quantity from POST (default 1)
        quantity = int(request.POST.get('quantity', 1))

        # Add/update movie in cart
        cart[str(movie.id)] = quantity

        # Save back to session
        request.session[cart_key] = cart

    return redirect('cart.index')


def clear(request):
    """
    Clear all carts.
    """
    for i in range(1, 4):
        request.session[f'cart{i}'] = {}
    return redirect('cart.index')


@login_required
def purchase(request):
    """
    Purchase movies from a specific cart (default cart1 if none specified).
    """
    # Example: only purchase from cart1
    cart = request.session.get('cart1', {})
    movie_ids = list(cart.keys())
    if not movie_ids:
        return redirect('cart.index')

    movies_in_cart = Movie.objects.filter(id__in=movie_ids)
    cart_total = calculate_cart_total(cart, movies_in_cart)

    order = Order(user=request.user, total=cart_total)
    order.save()

    for movie in movies_in_cart:
        item = Item(
            movie=movie,
            price=movie.price,
            order=order,
            quantity=cart[str(movie.id)]
        )
        item.save()

    # Clear cart1 after purchase
    request.session['cart1'] = {}

    template_data = {
        'title': 'Purchase confirmation',
        'order_id': order.id
    }
    return render(request, 'cart/purchase.html', {'template_data': template_data})
