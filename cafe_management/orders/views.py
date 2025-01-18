from django.views.generic import CreateView, DeleteView, FormView
from .forms import OrderForm, OrderDeleteForm
from .models import Order

class OrderCreateView(CreateView):
    form_class = OrderForm
    model = Order
    template_name = 'orders_create.html'
    title_page = 'Добавление заказа'

    def form_valid(self, form):
        table_number = form.cleaned_data['table_number']
        items = form.cleaned_data['items']
        order = Order.objects.create(table_number=table_number)
        order.items.set(items)
        return super().form_valid(form)


class OrderDeleteFormView(FormView):
    template_name = 'orders_delete.html'
    form_class = OrderDeleteForm

    def form_valid(self, form):
        order_id = form.cleaned_data['order_id']
        try:
            order = Order.objects.get(pk=order_id)
            order.delete()
            return super().form_valid(form)
        except Order.DoesNotExist:
            form.add_error('order_id', 'Заказ с указанным ID не найден.')
            return self.form_invalid(form)
