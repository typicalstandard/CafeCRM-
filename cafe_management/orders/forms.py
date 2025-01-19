from django import forms
from .models import Order
from menu.models import Dish

from .validators import validate_order_id


class OrderForm(forms.ModelForm):
    table_number = forms.IntegerField(required=True, label='Номер стола')
    items = forms.ModelMultipleChoiceField(
        queryset=Dish.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Список блюд',
        required=True
    )

    class Meta:
        model = Order
        fields = ['table_number', 'items']

    def clean_items(self):
        items = self.cleaned_data.get('items')
        if not items:
            raise forms.ValidationError('Необходимо выбрать хотя бы одно блюдо.')
        return items


class OrderDeleteForm(forms.Form):
    order_id = forms.IntegerField(label='Введите ID заказа для удаления', required=True,validators=[validate_order_id])





class OrderSearchForm(forms.Form):
    table_number = forms.IntegerField(required=False, label='Номер стола')
    status = forms.ChoiceField(choices=[
        ('waiting', 'в ожидании'),
        ('ready', 'готово'),
        ('paid', 'оплачено')
    ], required=False, label='Статус заказа')


class OrderStatusForm(forms.Form):
    order_id = forms.IntegerField(label='ID заказа',validators=[validate_order_id])
    status = forms.ChoiceField(label='Статус заказа', choices=[
        ('waiting', 'в ожидании'),
        ('ready', 'готово'),
        ('paid', 'оплачено')
    ])

