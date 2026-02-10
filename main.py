import requests
from bs4 import BeautifulSoup
import csv

response = requests.get('https://realpython.github.io/fake-jobs/')
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')
job_cards = soup.find_all('div', class_='card')

jobs = []
for card in job_cards:
    try:
        title = card.find(class_='title')
        title = title.text.strip() if title else 'N/A'
        
        company = card.find(class_='company')
        company = company.text.strip() if company else 'N/A'
        
        location = card.find(class_='location')
        location = location.text.strip() if location else 'N/A'
        
        apply_button = card.find(class_='card-footer-item', string='Apply')
        job_url = apply_button['href'] if apply_button and apply_button.get('href') else 'N/A'

        jobs.append({
            'title': title,
            'company': company,
            'location': location,
            'url': job_url
        })
    except Exception as e:
        print(f'Error parsing job card: {e}')
        continue

#Save to CSV
with open('./jobs.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['title', 'company', 'location', 'url'])
    writer.writeheader()
    writer.writerows(jobs)

print(f'Saved {len(jobs)} jobs to jobs.csv')