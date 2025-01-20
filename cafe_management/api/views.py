from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrderSerializer
from orders.models import Order


class CreateOrderAPIView(APIView):
    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class DeleteOrderAPIView(APIView):
    def delete(self, request, pk, format=None):
        try:
            order = Order.objects.get(pk=pk)
            order.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Order.DoesNotExist:
            return Response({'error': 'Заказ не найден'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class SearchOrderAPIView(APIView):
    def get(self, request, format=None):
        table_number = request.query_params.get('table_number')
        status_param = request.query_params.get('status')

        if table_number is not None:
            orders = Order.objects.filter(table_number=table_number)
        elif status_param is not None:
            orders = Order.objects.filter(status=status_param)
        else:
            return Response({'error': 'Table number or status not provided'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderUpdateStatusAPIView(APIView):
    def patch(self, request, pk, format=None):
        try:
            order = Order.objects.get(pk=pk)
            new_status = request.data.get('status')
            if new_status in ['waiting', 'ready', 'paid']:
                order.status = new_status
                order.save()
                return Response({'status': 'Статус обновлен'}, status=status.HTTP_200_OK)
            return Response({'error': 'Неверный статус'}, status=status.HTTP_400_BAD_REQUEST)
        except Order.DoesNotExist:
            return Response({'error': 'Заказ не найден'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
