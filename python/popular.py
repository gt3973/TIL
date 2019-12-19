import requests
import bs4

html = requests.get('https://www.naver.com/')

soup = bs4.BeautifulSoup(html.text,'html.parser')

keywords = soup.select('span.ah_k')

#print(len(keywords))

#for keyword in keywords:
#    print(keyword.text)

#배열[0:n] -> 배열의 0번쨰 인덱스부터 n-1번쨰까지
real_keywords = keywords[0:20]
real_real_keywords = [keyword.text for keyword in real_keywords]

#print(real_real_keywords)

problem = sorted(real_real_keywords)

answer = input('당신이 입력한 답: ')

if answer == real_real_keywords[0]:
    print('정답')
else :
    print('땡')



#numbers =[i for i in range(0,101)]
#print(numbers)
