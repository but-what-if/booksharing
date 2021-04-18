import csv

from parser import result
from time import time


with open(f'./jobs{time()}.csv', 'w') as file:
    fieldnames = ['id', 'title', 'salary', 'description']
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_writer.writeheader()
    for item in result:
        salary = ''.join(''.join(item['job_salary'].split(' ')).split(' '))
        csv_writer.writerow({
            'id': item['job_id'],
            'title': item['job_title'],
            'salary': salary,
            'description': item['job_description']
        })
