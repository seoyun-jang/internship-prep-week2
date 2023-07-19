
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