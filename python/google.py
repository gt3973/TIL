from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = './chromedriver.exe'
driver = webdriver.Chrome()
driver.get('https://www.google.com/')

search_input = driver.find_element_by_css_selector('#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')
search_input.send_keys('hello world')
search_input.send_keys(Keys.RETURN)
