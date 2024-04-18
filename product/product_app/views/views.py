from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from product.product_app.models.product_model import Product
from product.product_app.serializers.serializer import ProductSerializer

from rest_framework import status

from django.shortcuts import get_object_or_404


@api_view(['GET'])
def product_list(request) -> Response:
    """ List all products, or create a new product. """
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def product_detail(request) -> Response:
    """ Get a product instance. """
    product = get_object_or_404(Product, pk=request.query_params.get('id'))
    serializer = ProductSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)


def product_exists(request) -> Response:
    """ Check if a product exists. """
    product_id = request.query_params.get('id')
    exists = Product.objects.filter(id=product_id).exists()
    return Response({'exists': exists}, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def is_staff(request) -> bool:
    """ Check if a user is a staff user. """
    token_key = request.headers.get('Authorization').split()[1]
    token = Token.objects.get(key=token_key)
    user = token.user

    return user.is_staff


@api_view(['POST'])
def product_create(request) -> Response:
    """ Create a new product. """
    if is_staff(request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response('Fail to create product.', status=status.HTTP_403_FORBIDDEN)


@api_view(['DELETE'])
def product_delete(request) -> Response:
    """ Delete a product. """
    if is_staff(request):
        product = get_object_or_404(Product, pk=request.query_params.get('id'))
        product.delete()
        return Response('Success deleted.', status=status.HTTP_200_OK)
    return Response('Fail to delete product.', status=status.HTTP_403_FORBIDDEN)
