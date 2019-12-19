#로또 번호를 랜덤으로 뽑아주는 프로그램
import random


lotto = {
    '1번쨰' : random.randrange(1,46),
    '2번쨰' : random.randrange(1,46),
    '3번쨰' : random.randrange(1,46),
    '4번쨰' : random.randrange(1,46),
    '5번쨰' : random.randrange(1,46),
}

for i in range(0,5):
    print('{} : {}'.format(lotto[i].keys,lotto[i].values))

"""
numbers = range(1,46)

lotto = random.sample(numbers,6)
print(sorted(lotto))
"""
