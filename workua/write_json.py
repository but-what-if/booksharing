import json

from parser import result
from time import time


with open(f'./jobs{time()}.json', 'w') as file:
    all_data = []
    for item in result:
        salary = ''.join(''.join(item['job_salary'].split(' ')).split(' '))
        data = {f"id-{item['job_id']}": {
            'title': item['job_title'],
            'salary': salary,
            'description': item['job_description']
            }
        }
        all_data.append(data)
    json.dump(all_data, file, indent=4, ensure_ascii=False)
