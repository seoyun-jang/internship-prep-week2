
print('hello')

# variable
a = 10
b = 5
c = "hello"

print(a + b) 

a = 500
a += 50 # a = a + 50
print(a)

a -= 50 # a = a - 50
print(a)

print(abs(-5.3))
print(pow(3, 2))

# 화면에 *기호 100개 출력하기
print("*" * 100)

print("*** " * 20)
happyface = '😀'
print(happyface)

a = "3"
b = "5"
print(a + b)

a = 7
b = "5"

print(type(a))
print(type(b))
print(type(3.6))
print(type(True))


# string을 정수형, 실수형, 복수형으로 변환하기
a = "256"
print(int(a), type(int(a)))
print(float(a), type(float(a)))

a = [1, 2, 3]
a[0] = 4
print(a)

# list의 요소 삭제하기
del a[2]
print(a)

# list에 요소 추가하기
a = [0, 1, 2, 3, 4]
a.append(5)
a.append(6)
print(a)

# list에 다른 list의 요소를 추가하기
list2 = ["a", "b", "c", "d"]
a.extend(list2)
print(a)

# list 정렬
## sort / sorted
a = [6, 3, 10, 84, 30, 45, 13]
a.sort()
print(a)

sorted(a)
print(a)

## 역순으로 정렬 reverse
b = ["a", "b", "c", "A", "B"]
b.reverse()
print(b)

a.insert(3, "0")
print(a)

# list 요소 제거
## list의 첫번째 요소 제거
a.remove(30)
print(a)

## list의 특정 index 요소 제거 a.pop(index)
a.pop() # defualt : list의 마지막 요소
print(a)

a.pop(0)

# dictionary
## dictionary 선언
my_dictionary = dict()
my_dictionary = {}
print(my_dictionary)


### my_dictionary = {"key" : "value"}
my_dictionary = {"name" : "David",
                 "age" : 34}

## dictionary 요소 추가하기
my_dictionary["location"] = "seoul"
my_dictionary["number"] = [12, 34, 52]
my_dictionary["favorit_foods"] = [{"name":"pizza"}, {"name":"hamburger"}]
my_dictionary

## get
print(my_dictionary["name"])
print(my_dictionary.get("age", "Unknown"))

## key, value
print(my_dictionary.items())
print(my_dictionary.keys())
print(my_dictionary.values())
for key, value in my_dictionary.items():
    print("key : ", key)
    print("value : ", value)

# 
print("age" in my_dictionary)

# set
my_set = {1, 2, 3, 4, 5}

## set -> list, list -> set이 가능하다
## set에는 중복된 요소가 포함될 수 없다.
print(list(my_set))

example = "hello"
my_set = set(example)
print(my_set)

## set에 요소 추가
my_set.add(6)
print(my_set)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

print(set1 & set2)
print(set1 | set2)
print(set1 - set2)


# if-else문
"""
if A:
    조건이 참일때 수행할 표현
elif B:
    조건이 참일 때 수행할 표현 (A는 False)
else:
    A도 B도 아닌 경우 수행할 표현
    """

# while문
a = 5

while a > 0:
    print('hello')
    a -= 1

print("a : ", a)

a = -5
while a < 0:
    print("a is below 0")
    a += 1


# for문
my_list = ["A", "B", "C", "D"]
for letter in my_list:
    print(letter)

for i in range(5):
    print(i)
"""
.js
for (let i = 0; i<5; i++){

}
"""
for i in range(len(my_list)):
    print(my_list[i])

# Function
## js와 유사함
"""
# js.
function functionName(){

}


# python
def function_name():
    print(~)
"""

# def say_hello(name):
#     if not isinstance(my_list, list):
#         print("Error")
#         return
#     for name in my_list:

# say_hello("Mike")
