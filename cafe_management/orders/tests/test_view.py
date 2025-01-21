import pytest
from django.urls import reverse
from orders.models import Order

@pytest.mark.django_db
def test_order_create_view_get(client):
    url = reverse('order_create')
    response = client.get(url)
    assert response.status_code == 200
    assert 'orders_create.html' in [t.name for t in response.templates]
    assert 'form' in response.context

@pytest.mark.django_db
def test_order_create_view_post_valid(client,dish):
    url = reverse('order_create')
    form_data = {
        'table_number': 1,
        'items': [dish.id],
    }
    response = client.post(url, data=form_data)
    assert response.status_code == 302
    assert response.url == reverse('home')
    assert Order.objects.count() == 1
    assert Order.objects.first().status == 'waiting'


@pytest.mark.django_db
def test_order_create_view_post_invalid(client):
    url = reverse('order_create')
    form_data = {
        'table_number': '',
        'total_price': 100.00,
        'status': 'waiting'
    }
    response = client.post(url, data=form_data)
    assert response.status_code == 200
    assert 'form' in response.context
    assert 'table_number' in response.context['form'].errors
    assert response.context['form'].errors['table_number'] == ['This field is required.']


@pytest.mark.django_db
def test_order_delete_view_get(client):
    url = reverse('order_delete')
    response = client.get(url)
    assert response.status_code == 200
    assert 'orders_delete.html' in [t.name for t in response.templates]
    assert 'form' in response.context

@pytest.mark.django_db
def test_order_delete_view_post_valid(client, order):
    url = reverse('order_delete')
    form_data = {
        'order_id': order.id,
    }
    response = client.post(url, data=form_data)
    assert response.status_code == 302
    assert response.url == reverse('home')
    assert Order.objects.count() == 0

@pytest.mark.django_db
def test_order_delete_view_post_invalid(client):
    url = reverse('order_delete')
    form_data = {
        'order_id': '',
    }
    response = client.post(url, data=form_data)
    assert response.status_code == 200
    assert 'form' in response.context
    assert 'order_id' in response.context['form'].errors
    assert response.context['form'].errors['order_id'] == ['This field is required.']



@pytest.mark.django_db
def test_order_update_view_get(client):
    url = reverse('order_update')
    response = client.get(url)
    assert response.status_code == 200
    assert 'orders_choice_status.html' in [t.name for t in response.templates]
    assert 'form' in response.context


@pytest.mark.django_db
def test_order_update_view_post_valid(client, order):
    url = reverse('order_update')
    form_data = {
        'order_id': order.id,
        'status': 'ready'
    }
    response = client.post(url, data=form_data)
    assert response.status_code == 302
    assert response.url == reverse('home')
    order.refresh_from_db()
    assert order.status == 'ready'


@pytest.mark.django_db
def test_order_update_view_post_invalid(client):
    url = reverse('order_update')
    form_data = {
        'order_id': '',
        'status': 'ready'
    }
    response = client.post(url, data=form_data)
    assert response.status_code == 200
    assert 'form' in response.context
    assert 'order_id' in response.context['form'].errors
    assert response.context['form'].errors['order_id'] == ['This field is required.']

@pytest.mark.django_db
def test_order_search_by_table_number(client, orders):
    response = client.get(reverse('home') + '?query=1')
    assert response.status_code == 200
    assert len(response.context['orders']) == 2

@pytest.mark.django_db
def test_order_search_by_status(client, orders):
    response = client.get(reverse('home') + '?query=waiting')
    assert response.status_code == 200
    assert len(response.context['orders']) == 1

@pytest.mark.django_db
def test_order_search_by_exact_status(client, orders):
    response = client.get(reverse('home') + '?status=ready')
    assert response.status_code == 200
    assert len(response.context['orders']) == 2

@pytest.mark.django_db
def test_order_search_combined(client, orders):
    response = client.get(reverse('home') + '?query=1&status=ready')
    assert response.status_code == 200
    assert len(response.context['orders']) == 1
