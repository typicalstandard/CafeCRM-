from django.views.generic import CreateView, DeleteView, FormView, ListView
from .forms import OrderForm, OrderDeleteForm, OrderSearchForm
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




class OrderSearchView(ListView):
    model = Order
    template_name = 'orders_search.html'
    context_object_name = 'orders'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        table_number = self.request.GET.get('table_number')
        status = self.request.GET.get('status')
        if table_number:
            queryset = queryset.filter(table_number=table_number)
        if status:
            queryset = queryset.filter(status=status)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = OrderSearchForm(self.request.GET or None)
        return context
