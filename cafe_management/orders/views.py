from django.views.generic import CreateView, DeleteView, FormView
from .forms import OrderForm
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


