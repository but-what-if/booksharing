import sqlite3

from parser import result


con = sqlite3.connect('jobs_base.db')
cur = con.cursor()

cur.execute('''CREATE TABLE jobs_base
               (id VARCHAR2, title VARCHAR2, salary VARCHAR2, description VARCHAR2)''')
for item in result:
    salary = ''.join(''.join(item['job_salary'].split(' ')).split(' '))
    cur.execute(f"INSERT INTO jobs_base VALUES (?,?,?,?)", (f"{item['job_id']}", f"{item['job_title']}", f"{salary}", f"{item['job_description']}"))

con.commit()

con.close()
