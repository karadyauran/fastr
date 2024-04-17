import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from authentication.authenticate.models import UserAuth


@pytest.fixture
def test_api_client():
    return APIClient()


@pytest.fixture
def test_user_data():
    return {
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'testpassword'
    }


@pytest.mark.django_db
def test_test_signup_success(api_client, user_data):
    url = reverse('signup')
    response = api_client.post(url, user_data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert 'token' in response.data
    assert 'user' in response.data

    user = UserAuth.objects.get(username=user_data['username'])
    assert user is not None


@pytest.mark.django_db
def test_signup_invalid_data(api_client):
    url = reverse('signup')
    invalid_data = {
        'username': '',
        'email': 'test@example.com',
        'password': ''
    }
    response = api_client.post(url, invalid_data, format='json')

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'username' in response.data
    assert 'password' in response.data
