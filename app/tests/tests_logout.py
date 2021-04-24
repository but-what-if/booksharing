from django.urls import reverse


def test_logout(client):
    url = reverse('logout')
    response = client.get(url)
    assert response.status_code == 302


