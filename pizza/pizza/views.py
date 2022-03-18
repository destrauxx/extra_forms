from django.shortcuts import render
from .models import PizzaModel
# Create your views here.

def pizza_detail_view(request, *args, **kwargs):
    print(kwargs)
    pizza_object = PizzaModel.objects.get(name_slug=kwargs.get('slug'))
    context = {'pizza_objects': pizza_object}
    return render(request, 'pizza/pizza_detail.html', context)