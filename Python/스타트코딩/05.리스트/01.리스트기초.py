#리스트 생성하기
animals = ["사자", "호랑이", "고양이", "강아지"]

#데이터 접근하기
name = animals[3]

#데이터 추가하기
animals.append("하마")
animals.append(1) #잘 쓰이지 않음

#데이터 삭제하기
del animals[-1] #-1은 마지막 데이터 삭제하기

#리스트 슬라이싱
slicing = animals[1:3]

#리스트 길이
length = len(animals)

#리스트 정렬
animals.sort(reverse=True) #sort() 오름차수 정렬 / sort(reverse=True) 내림차수 정렬

print(animals)