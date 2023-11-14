#1.로또 번호 6개를 생성
#2.로또 번호는 1~45까지의 랜덤한 번호
#3.6개의 숫자 모두 달라야 한다
#4.로또 번호 생성함수를 작성하고 사용한다
import random 

lotto_num = [] #빈 로또 번호 히스트 생성

def getRandomNumber():
    number = random.randint(1,45)
    return number

count = 0 # 횟수를 저장할 변수

#무한반복
while True:
    if count > 5:
        break
    random_number = getRandomNumber() # 로또 번호 하나를 뽑는다
    if random_number not in lotto_num: # 로또 번호 리스트 안에 뽑은 로또 번호가 없으면
        lotto_num.append(random_number) # 로또 번호 히스트에 뽑은 로또 번호를 추가해라
        count = count + 1

print(lotto_num)
