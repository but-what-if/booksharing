from django.urls import reverse


def test_profile(client):
    url = reverse('my-profile')

    response = client.get(url)
    assert response.status_code == 302

    payload = {
        'firstname': 'adminDadmin.com',
        'lastname': 'adminDadmin.com',
    }
    response = client.post(url, data=payload)
    assert response.status_code == 302
