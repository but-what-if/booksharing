from django.core.management.base import BaseCommand
from faker import Faker
import random
from datetime import datetime
from books.models import Book, Author, Category


class Command(BaseCommand):
    help = 'Generate Random Book'  # noqa

    def add_arguments(self, parser):
        parser.add_argument('amount', type=int)

    def handle(self, *args, **kwargs):
        fake = Faker()
        amount = kwargs['amount']
        authors = []
        for _ in range(amount):
            first_name = fake.word().capitalize()
            last_name = fake.word().capitalize()
            date_of_birth = fake.date()
            date_of_death = fake.date()
            country = fake.country()
            gender = random.choice(['Male', 'Female'])
            language = fake.word()
            authors.append(Author(
                first_name=first_name,
                last_name=last_name,
                date_of_birth=date_of_birth,
                date_of_death=date_of_death,
                country=country,
                gender=gender,
                language=language
            ))
        Author.objects.bulk_create(authors)

        books_list = []
        for _ in range(amount):
            author = Author.objects.order_by('?').last()
            title = fake.word()
            category = random.choice(Category.objects.all())
            publish_year = random.randint(0, datetime.now().year)
            review = fake.text()
            condition = random.randint(1, 5)
            books_list.append(Book(
                author=author,
                title=title,
                category=category,
                publish_year=publish_year,
                review=review,
                condition=condition,
            ))
        Book.objects.bulk_create(books_list)
