from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product, OrderItem, Order

# Create your views here.


def say_hello(request):

    # queryset = Product.objects.values_list ()

    # queryset = Product.objects.filter(
    #     id__in=OrderItem.objects.values("product_id")
    # ).order_by("title")
    # queryset = Product.objects.filter(unit_price__lt=500)
    # queryset = Product.objects.filter(Q(inventory__lt=10) | ~Q(unit_price__lt=500))

    # queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:3]


    return render(
        request,
        "hello.html",
        {"name": "Ali"},
    )
