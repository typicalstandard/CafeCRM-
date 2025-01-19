from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, DeleteView, FormView, ListView, UpdateView
from .forms import OrderForm, OrderDeleteForm, OrderSearchForm, OrderStatusForm
from .models import Order

class OrderCreateView(CreateView):
    form_class = OrderForm
    model = Order
    template_name = 'orders_create.html'
    title_page = 'Добавление заказа'


class OrderDeleteFormView(FormView):
    template_name = 'orders_delete.html'
    form_class = OrderDeleteForm

    def form_valid(self, form):
        order_id = form.cleaned_data['order_id']
        order = Order.objects.get(pk=order_id)
        order.delete()
        return super().form_valid(form)

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



class OrderListView(ListView):
    model = Order
    template_name = 'home.html'
    context_object_name = 'orders'


class OrderUpdateView(FormView):
    template_name = 'orders_choice_status.html'
    form_class = OrderStatusForm

    def form_valid(self, form):
        order_id = form.cleaned_data['order_id']
        status = form.cleaned_data['status']
        order = Order.objects.filter(id=order_id).first()
        order.status = status
        order.save()
        return super().form_valid(form)




def total_revenue(request):
    paid_orders = Order.objects.filter(status='paid')
    total_revenue = sum(order.total_price for order in paid_orders)
    return render(request, 'total_revenue.html', {'total_revenue': total_revenue})
