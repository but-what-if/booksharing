from django.urls import reverse


def test_get_form(client):
    url = reverse('signup')
    response = client.get(url)
    assert response.status_code == 200


def test_empty_payload(client):
    url = reverse('signup')
    response = client.post(url, data={})
    assert response.status_code == 200
    assert response.context_data['form'].errors == {
        'email': ['This field is required.'],
        'password1': ['This field is required.'],
        'password2': ['This field is required.']
    }


def test_invalid_payload(client):
    url = reverse('signup')
    payload = {
        'email': 'invalid_email',
        'password1': 'dfdfdffef3e333',
        'password2': 'sscscsr33434',
    }
    response = client.post(url, data=payload)
    assert response.status_code == 200
    assert response.context_data['form'].errors == {
        'email': ['Enter a valid email address.'],
        'password2': ['Passwords should match!']
    }


def test_valid_payload(client, mailoutbox):
    url = reverse('signup')
    payload = {
        'email': 'validemail@mail.com',
        'password1': 'dfdfdffef3e333',
        'password2': 'dfdfdffef3e333',
    }
    response = client.post(url, data=payload, follow=True)
    assert response.status_code == 200
    assert response.redirect_chain == [('/', 302)]
