import pytest
from orders.forms import OrderDeleteForm, OrderStatusForm, OrderSearchForm,OrderForm





@pytest.mark.django_db
def test_order_form_valid(dish):
    form_data = {
        'table_number': 1,
        'items': [dish.id]
    }
    form = OrderForm(data=form_data)
    assert form.is_valid()

@pytest.mark.django_db
def test_order_form_invalid(dish):
    form_data = {
        'table_number': 1,
        'items': []
    }
    form = OrderForm(data=form_data)
    assert not form.is_valid()
    assert 'Необходимо выбрать хотя бы одно блюдо.' in form.errors['items']

@pytest.mark.django_db
def test_order_form_invalid_table_number(dish):
    form_data = {
        'table_number': -1,
        'items': [dish.id]
    }
    form = OrderForm(data=form_data)
    assert not form.is_valid()
    assert 'Номер стола должен быть положительным числом.' in form.errors['table_number']


@pytest.mark.django_db
def test_order_form_invalid_table_number_type(dish):
    form_data = {
        'table_number': 'invalid_type',
        'items': [dish.id]
    }
    form = OrderForm(data=form_data)
    assert not form.is_valid()
    assert 'Введите допустимое целое число.' in form.errors['table_number']



@pytest.mark.django_db
def test_order_delete_form_valid(order):
    form_data = {
        'order_id': order.id
    }
    form = OrderDeleteForm(data=form_data)
    assert form.is_valid()


@pytest.mark.django_db
def test_order_delete_form_invalid():
    form_data = {
        'order_id': 999999
    }
    form = OrderDeleteForm(data=form_data)
    assert not form.is_valid()
    assert 'Заказ с указанным ID не найден.' in form.errors['order_id']
@pytest.mark.django_db
def test_order_delete_form_invalid_negative():
    form_data = {
        'order_id': 'invalid_type'
    }
    form = OrderDeleteForm(data=form_data)
    assert not form.is_valid()
    assert 'Введите допустимое целое число.' in form.errors['order_id']

@pytest.mark.django_db
def test_order_delete_form_invalid_type():
    form_data = {
        'order_id': -1
    }
    form = OrderDeleteForm(data=form_data)
    assert not form.is_valid()
    assert 'ID заказа должно быть положительным числом.' in form.errors['order_id']


@pytest.mark.django_db
def test_order_search_form_valid():
    form_data = {
        'table_number': 1,
        'status': 'waiting'
    }
    form = OrderSearchForm(data=form_data)
    assert form.is_valid()




@pytest.mark.django_db
def test_order_status_form_valid(order):
    form_data = {
        'order_id': order.id,
        'status': 'ready'
    }
    form = OrderStatusForm(data=form_data)
    assert form.is_valid()


@pytest.mark.django_db
def test_order_status_form_invalid_order_id():
    form_data = {
        'order_id': '',
        'status': 'ready'
    }
    form = OrderStatusForm(data=form_data)
    assert not form.is_valid()
    assert 'order_id' in form.errors
