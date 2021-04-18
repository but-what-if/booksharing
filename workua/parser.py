import requests
from bs4 import BeautifulSoup
from time import time, sleep
import random
from fake_useragent import UserAgent

ua = UserAgent()
BASE_URL = f'https://www.work.ua/jobs/'
PAGE = 0


def random_sleep():
    sleep(random.randint(1, 3))


result = []


def collect_data(url: str, page: int = 0) -> list:
    # while True:
    for _ in range(2):
        page += 1

        params = {
            'ss': 1,
            'page': page,
        }
        headers = {
            'User-Agent': ua.random,  # user-agent == 'python-3.9'
        }
        response = requests.get(url, params=params, headers=headers)

        random_sleep()

        response.raise_for_status()  # stop program if status_code != 2xx

        html = response.text

        soup = BeautifulSoup(html, 'html.parser')
        jobs_list = soup.find(id="pjax-job-list")

        if jobs_list is None:
            break

        cards = jobs_list.find_all("div", {"class": "job-link"})

        for card in cards:
            tag_a = card.find("h2").find("a")
            job_id = tag_a['href'].split('/')[-2]

            card_url = f'https://www.work.ua/jobs/{job_id}/'
            response = requests.get(card_url)
            card_html = response.text

            soup = BeautifulSoup(card_html, 'html.parser')
            job_title = soup.find(id="h1-name").text
            salary_tag = soup.find("span", {"title": "Зарплата"})

            if salary_tag is not None:
                job_salary = salary_tag.find_next_sibling("b")
                if job_salary is not None:
                    job_salary = ''.join(job_salary.text.split('THSP'))
            else:
                job_salary = ''

            job_description = soup.find(id="job-description").text

            result.append({
                'job_id': f'{job_id}',
                'job_title': f'{job_title}',
                'job_salary': f'{job_salary}',
                'job_description': f'{job_description}'
            })

    return result


collect_data(BASE_URL, PAGE)
