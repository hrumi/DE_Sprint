import time

from bs4 import BeautifulSoup
import requests
import lxml
import json

url = "https://spb.hh.ru/search/vacancy?search_field=name&text=Python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&from=suggest_post"
headers = {'User-Agent': 'Mozilla/5.0', 'Host': 'kemerovo.hh.ru'}
resp = requests.get(url, headers=headers)
soup = BeautifulSoup(resp.text, "lxml")

lastTag = soup.findAll('a', {'rel': 'nofollow', 'data-qa': 'pager-page'})
maxPage = int(lastTag[len(lastTag) - 1].text)
pageLink = "https://spb.hh.ru" + lastTag[len(lastTag) - 1].get('href')

data = {
    'data': []
}

i = 0
while i < maxPage:
    if i == 0:
        urlPage = url
    else:
        urlPage = url + '&page=' + str(i) + '&hhtmFrom=vacancy_search_list'
    i = i + 1
    respPage = requests.get(urlPage, headers=headers)
    soup = BeautifulSoup(resp.text, "lxml")
    vacancies = soup.findAll('a', class_='serp-item__title')

    for vacancy in vacancies:
        time.sleep(2)
        vacancyLink = vacancy.get('href')
        respVacancy = requests.get(vacancyLink, headers=headers)
        soupVacancy = BeautifulSoup(respVacancy.text, "lxml")

        nameVacancy = soupVacancy.find(attrs={'data-qa': 'vacancy-title'}).text
        experienceVacancy = soupVacancy.find(attrs={'data-qa': 'vacancy-experience'}).text
        salaryVacancy = soupVacancy.find(attrs={'data-qa': 'vacancy-salary-compensation-type-net'})
        if salaryVacancy is not None:
            salaryVacancy = salaryVacancy.text
        placeVacancy = soupVacancy.find(attrs={'data-qa': 'vacancy-view-raw-address'})
        if placeVacancy is not None:
            placeVacancy = placeVacancy.text

        data['data'].append({'Title': nameVacancy, 'Experience': experienceVacancy, 'Salary': salaryVacancy, 'Place': placeVacancy})
        with open('data.json', 'w') as file:
            json.dump(data, file, ensure_ascii=False)
