import requests
from bs4 import BeautifulSoup

url = "https://bank.gov.ua/ua/markets/exchangerates"
r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")
soup_list_liter = soup.find_all('td',{'data-label':"Код літерний"})
soup_list_count = soup.find_all('td',{'data-label':"Кількість одиниць валюти"})
soup_list_course = soup.find_all('td',{'data-label':"Офіційний курс"})

f = open("hw10.txt","a")
for line in range(len(soup_list_liter)):
    s = f"{soup_list_liter[line].text}\t {soup_list_count[line].text} : {soup_list_course[line].text} \n"
    print(s, end="")
    f.write(s)
f.close()