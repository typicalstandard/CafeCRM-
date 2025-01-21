from django import forms
from .models import Order
from menu.models import Dish

from .validators import validate_order_id


class OrderForm(forms.ModelForm):
    table_number = forms.IntegerField(
          required=True,
          label='Номер стола',
          min_value=1,
          error_messages={
              'invalid': 'Введите допустимое целое число.',
              'min_value': 'Номер стола должен быть положительным числом.'
          }
    )
    items = forms.ModelMultipleChoiceField(
        queryset=Dish.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Список блюд',
        required=True,
        error_messages={
            'required': 'Необходимо выбрать хотя бы одно блюдо.'
        }
    )

    class Meta:
        model = Order
        fields = ['table_number', 'items']



class OrderDeleteForm(forms.Form):
    order_id = forms.IntegerField(
          label='Введите ID заказа для удаления',
          required=True,
          min_value=1,
          error_messages={
              'invalid': 'Введите допустимое целое число.',
              'min_value': 'ID заказа должно быть положительным числом.'
          },
          validators=[validate_order_id]
    )


class OrderSearchForm(forms.Form):
    query = forms.CharField(
        label='Поиск по номеру стола или статусу',
        max_length=100,
        required=False,
        help_text='Введите номер стола или статус'
    )
    status = forms.ChoiceField(
        choices=[
            ('','------'),
            ('waiting', 'в ожидании'),
            ('ready', 'готово'),
            ('paid', 'оплачено')
        ],
        required=False,
        label='Статус заказа',
        error_messages={
            'invalid_choice': 'Выберите допустимое значение. %(value)s недоступно.',
        }
    )




class OrderStatusForm(forms.Form):
    order_id = forms.IntegerField(
          label='ID заказа',
          required=True,
          min_value = 1,
          error_messages = {
                'invalid': 'Введите допустимое целое число.',
                'min_value': 'ID заказа должно быть положительным числом.'
          },
          validators=[validate_order_id]
    )
    status = forms.ChoiceField(
           label='Статус заказа',
           choices=[
               ('waiting', 'в ожидании'),
               ('ready', 'готово'),
               ('paid', 'оплачено')
           ],
           required=True,
           error_messages=
           {
            'invalid_choice': 'Выберите допустимое значение. %(value)s недоступно.',
            }
    )
