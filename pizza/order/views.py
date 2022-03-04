from django.shortcuts import redirect, render

from pizza.models import PizzaModel
from .models import OrderModel
from .forms import CreateForm, CreateOrderModelForm

# Create your views here.

def create_order(request, *args, **kwargs):
    pizzas = PizzaModel.objects.all()
    order_form = CreateForm(request.POST or None)
    if order_form.is_valid():
        address = order_form.cleaned_data.get('address')
        order = dict(order_form.data).get('choice')
        pizza_objects = [PizzaModel.objects.get(id=i) for i in order]
        new_order = OrderModel.objects.create(address=address)
        new_order.pizza_order.add(*pizza_objects)
        new_order.save()
        return redirect('create_order')

    context = {
        'pizza': pizzas,
        'order_form': order_form
    }
    return render(request, 'order/create_order.html', context=context)

def create_model_order(request, *args, **kwargs):
    pizzas = PizzaModel.objects.all()
    model_form = CreateOrderModelForm(request.POST or None)

    if model_form.is_valid():
        model_form.save()
        return redirect('createmodelorder')
        
    context = {
        'pizza': pizzas,
        'modelform': model_form,
    }
    return render(request, 'order/create_model_order.html', context=context)