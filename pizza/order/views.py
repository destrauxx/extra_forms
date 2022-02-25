from django.shortcuts import render

from pizza.models import PizzaModel
from .forms import CreateForm

# Create your views here.

def create_order(request, *args, **kwargs):
    pizza = PizzaModel.objects.all()
    order_form = CreateForm(request.POST or None)
    context = {
        'pizza': pizza,
        'order_form': order_form
    }
    return render(request, 'order/create_order.html', context=context)