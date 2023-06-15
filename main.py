from bs4 import BeautifulSoup
import requests
import time

print("Put some skills that you are not familiar with")
unfamiliar_skills = input('>')
print(f"filtering out {unfamiliar_skills}")


def get_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_ = 'sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
            link = job.header.h2.a['href']
            if unfamiliar_skills not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Skills: {skills.strip()} \n")
                    f.write(f"More Info: {link}")
                    print(f"File saved: {index}")

while True:
    get_jobs()
    wait_time = 10
    print(f"Waiting {wait_time} minutes")
    time.sleep(wait_time * 60)

