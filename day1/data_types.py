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

# string에서 특정 문자열 바꾸기


# string의 길이를 구하고 중복되는 문자의 갯수 출력하기
txt = "lalalalalalalalalala"
print(len(txt))
print(txt.count("a"))



