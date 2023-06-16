from bs4 import BeautifulSoup
import requests, openpyxl
import time

excel = openpyxl.Workbook()
sheet = excel.active

sheet.title = "Python Jobs"
print(excel.sheetnames)
sheet.append(["Company Name", "Skills", "Link"])

print("Put some skills that you are not familiar with")
unfamiliar_skills = input('>')
print(f"filtering out {unfamiliar_skills}")



def get_jobs():
    try:
        html_page = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')

        html_page.raise_for_status()
        soup = BeautifulSoup(html_page.text, 'lxml')
        jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

        for index, job in enumerate(jobs):
            published_date = job.find('span', class_ = 'sim-posted').span.text
            if 'few' in published_date:
                company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '').strip()
                skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '').strip()
                link = job.header.h2.a['href']
                if unfamiliar_skills not in skills:
                    print(company_name, skills, link)
                    sheet.append([company_name, skills, link])
                    # with open(f'posts/{index}.txt', 'w') as f:
                    #     f.write(f"Company Name: {company_name.strip()} \n")
                    #     f.write(f"Skills: {skills.strip()} \n")
                    #     f.write(f"More Info: {link}")
                    #     print(f"File saved: {index}")

    except Exception as e:
        print(e)

    excel.save("Timesjobs python jobs.xlsx")


while True:
    get_jobs()
    wait_time = 10
    print(f"Waiting {wait_time} minutes")
    time.sleep(wait_time * 60)

