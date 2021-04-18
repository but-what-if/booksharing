import sqlite3

from parser import result


con = sqlite3.connect('jobs.db')
cur = con.cursor()

cur.execute('''CREATE TABLE jobs
               (id, title, salary, description)''')
for item in result:
    salary = ''.join(''.join(item['job_salary'].split(' ')).split(' '))
    # cur.execute("INSERT INTO jobs VALUES ({0},{1},{2},{3})".format(item['job_id'], item['job_title'], salary, item['job_description']))
    cur.execute(f"INSERT INTO jobs VALUES ({item['job_id']}, {item['job_title']}, {salary}, {item['job_description']})")
    # cur.execute("INSERT INTO jobs VALUES (%s, %s, %s, %s)", item['job_id'], item['job_title'], salary, item['job_description'])

con.commit()

con.close()
