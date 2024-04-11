from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializer import ProductSerializer

from rest_framework import status
import requests

from django.shortcuts import get_object_or_404


@api_view(['GET'])
def product_list(request):
    """ List all products, or create a new product. """
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def product_detail(request):
    """ Get a product instance. """
    product = get_object_or_404(Product, pk=request.query_params.get('id'))
    serializer = ProductSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def product_exists(request):
    """ Check if a product exists. """
    product_id = request.query_params.get('id')
    exists = Product.objects.filter(id=product_id).exists()
    return Response({'exists': exists}, status=status.HTTP_200_OK)


def is_user_staff(request):
    """ Check if user is staff or not. """
    token = request.headers.get('Authorization')
    response = requests.get('http://127.0.0.1:8001/api/v3/user/is_staff', headers={'Authorization': token})
    if response.status_code == 200:
        is_staff = response.json()['is_staff']
        return is_staff
    return False


@api_view(['POST'])
def product_create(request):
    """ Create a new product. """
    if is_user_staff(request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response('Fail to create product.', status=status.HTTP_403_FORBIDDEN)


@api_view(['DELETE'])
def product_delete(request):
    """ Delete a product. """
    if is_user_staff(request):
        product = get_object_or_404(Product, pk=request.query_params.get('id'))
        product.delete()
        return Response('Success deleted.', status=status.HTTP_200_OK)
    return Response('Fail to delete product.', status=status.HTTP_403_FORBIDDEN)
