from django.contrib import admin

from .models import PizzaModel, ToppingsModel

# Register your models here.
class PizzaInline(admin.TabularInline):
    model = PizzaModel.toppings.through
    extra = 0

class PizzaAdmin(admin.ModelAdmin):
    inlines = [
        PizzaInline,
    ]
    exclude = ('toppings',)

admin.site.register(PizzaModel, PizzaAdmin)
admin.site.register(ToppingsModel)
