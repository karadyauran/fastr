from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializer import ProductSerializer

from rest_framework import status
import requests


@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def product_create(request):
    token = request.headers['Authorization']
    is_staff = requests.get('http://127.0.0.1:8001/api/v3/user/is_staff', headers={'Authorization': token})

    if is_staff.status_code == 200:
        is_staff_str = is_staff.text.strip()
        is_staff = is_staff_str.lower() == 'true'

        if is_staff:
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.create(request.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response('Fail to create product.', status=status.HTTP_403_FORBIDDEN)
    else:
        return Response('Fail to get info.', status=status.HTTP_403_FORBIDDEN)
