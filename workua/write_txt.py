from parser import result
from time import time


with open(f'./jobs{time()}.txt', 'w') as file:
    for item in result:
        salary = ''.join(''.join(item['job_salary'].split(' ')).split(' '))
        file.write(f"{item['job_id']} | {item['job_title']} | {salary} | {item['job_description']}\n\n")
