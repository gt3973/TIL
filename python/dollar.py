import requests
import bs4

html = requests.get('https://finance.naver.com/marketindex/?tabSel=exchange#tab_section')

soup = bs4.BeautifulSoup(html.text,'html.parser')

kospi = soup.select_one('#input_from_money')

print(kospi)