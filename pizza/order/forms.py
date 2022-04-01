from django import forms
from pizza.models import PizzaModel
from .models import OrderModel

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Button, ButtonHolder, Field
PIZZAS = [
    (f'{p.id}', f'{p.name}') for p in PizzaModel.objects.all()
]

DEL_STATUS = [('PEN', 'Pending'), ('DEL', 'Delivered')]

class CreateForm(forms.Form):
    address = forms.CharField(required=True)
    choice = forms.ChoiceField(
        choices=PIZZAS,
        help_text='If you want some extra. Send us <a href="#">Message</a>',
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'pizzas'}))
    delivery_status = forms.ChoiceField(
        choices=DEL_STATUS
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.form_method = 'post'
        


class CreateOrderModelForm(forms.ModelForm):
    error_css_class = 'error-field-class'
    required_css_class = 'required-field-class'

    class Meta:
        model = OrderModel
        fields = ['address', 'pizza_order']
        widgets = {
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your address:'
            }),
            'pizza_order': forms.CheckboxSelectMultiple()
        }
