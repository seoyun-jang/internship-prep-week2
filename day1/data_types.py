number_list = [1, 2, 3, 4]
names = ["Lukas", "David", "George", "Lee"]

random_list = [3, 3.6, "Python", False, [1, 2, 3]]
print(random_list)

for element in random_list:
    print(type(element))

# list
"""
대괄호[]를 사용하여 나타낸다
여러 datatype이 포함될 수 있다
재할당이 가능하다
"""
random_list = [1, 2, 3, 4]
print(random_list)

random_list[0] = 6
print(random_list)


# tuple
""" 
괄호()를 사용하여 나타낸다
여러 datatype이 포함될 수 있다
재 할당이 불가능하다
"""

my_tuple = (1, 2, "Python", 3.6, True)
# my_tuple[0] = 6

# string
# length를 구하는 len 함수
a = "Hello world 😀"
b = "ESG internship"

print(len(a))
print(len(b))

print(a[12])
print(a[0:0])
print(a[:5])
print(a[6:])

print(a.index("w"))

my_list = [1, 2, 5.5, "hello", [5, 6, 7, 8]]
print(my_list[3:6])

class_name = "chatGPT API"
print(class_name[4:])
print(class_name[:7])

find_str = "python!"

# find index
print(find_str.find("y"))

print(".".join(find_str))

# 문자 변환

## 대문자/소문자 변환
title = "PyThoN ClASs"

print(title.lower()) # 대문자 -> 소문자
print(title.upper()) # 소문자 -> 대문자

## 양쪽 공백 지우기
print(title.strip()) 

# replace : 문자 대체(바꾸기)
quote = "Life is too short"

print(quote.replace("too", "very"))
print(quote.replace("o", "0"))
print(quote.replace(" ",""))

# split : 문자 분해
# default .seplit(" ")
print(quote.split())

