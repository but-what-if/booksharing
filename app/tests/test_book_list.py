from django.urls import reverse


def test_book_list(client):
    url = reverse('books:list')
    response = client.get(url)
    assert response.status_code == 200
