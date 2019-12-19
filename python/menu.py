#랜덤으로 오늘의 점심메뉴를 추천해주는 프로그램
import random

menu = [ '새마을식당','초원삼겹살', '멀캠20층', '홍콩반점','순남시래기']

phone_book = {
    '새마을식당':'010-1234-1234',
    '초원삼겹살':'02-00-99',
    '멀캠20층':'02-123-123',
    '홍콩반점':'010-1234-1234',
    '순남시래기':'02-2222-2222'}

print(phone_book['새마을식당'])

#menu의 요소 중 랜덤으로 골라줌
lunch = random.choice(menu)

print(lunch)
print(phone_book[lunch])

#print(menu[random.randrange(0,5)])