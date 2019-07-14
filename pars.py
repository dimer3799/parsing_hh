# Парсинг hh.ru
import requests
from bs4 import BeautifulSoup as bs


def hh_parse(my_url, headers):
	session = requests.Session() # Открываем ссесию для доступа в инет
	request = session.get(my_url, headers = headers)  #Эмулируем открытие страницы в веб-браузере
	if request.status_code == 200:  # Условие если (страница отвечает и открылась) 
		print('Ok')
		data = bs(request.content, 'html.parser') 
		divs = data.find_all('div', attrs={'data-qa': 'vacancy-serp__vacancy'}) # Записываем ищем все вакансии на странице
		print(len(divs))
		i = 0
		for div in divs:
			i+=1 # Номер вакансии
			title = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'}).text # Название вакансии в заголовке
			href = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'})['href'] # Ссылки на вакунсию
			compani = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-employer'}).text # Название компании
			text1 = div.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_responsibility'}).text # Описание обязонности
			text2 = div.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_requirement'}).text # Требование к вакансии
			print(i,title) # Вывод названии вакансии
			print(compani)
			print("Обязонности: ",text1)
			print("Требование: ",text2)
			print(href,'\n') # Вывод ссылки на вакансию
	else:
		print('Error') # Если веб-страница не отвечает вывод надпись Error


headers = {'acept': '*/*',
			'user-agent':'Mozilla/5.0 (Windows NT 6.1; rv:68.0) Gecko/20100101 Firefox/68.0'
			}
			
my_url = 'https://tyumen.hh.ru/search/vacancy?text=python&area=95&page=0'
hh_parse(my_url, headers)

my_url = 'https://tyumen.hh.ru/search/vacancy?text=python&area=95&page=1'
hh_parse(my_url, headers)

my_url = 'https://tyumen.hh.ru/search/vacancy?text=python&area=95&page=2'
hh_parse(my_url, headers)

my_url = 'https://tyumen.hh.ru/search/vacancy?text=python&area=95&page=3'
hh_parse(my_url, headers)
