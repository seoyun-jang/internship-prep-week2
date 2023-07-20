
# abs
print(3)
print(-3.5)
print(-7)

print(abs(3))
print(abs(-3.5))
print(abs(-7))

# range
## range(start, stop, step)
for i in range(5):
    print(i)


for i in range(5, 10):
    print(i)

for i in range(0,10, 2):
    print(i)


# filter 
def positive(x):
    # bool type
    return x > 0

a = [1, 3, 0, -3, -6]

# print(positive(a))
"""positive 함수는 int와의 비교이지만 a는 list이기 때문에 비교가 불가능하다는 에러가 발생한다.
이와 같은 경우에 filter를 이용해 비교할 수 있게 한다.
"""
list(filter(positive, a))

# enumerate
colors = ["white", "red", "brown", "blue"]
names = ["Lukas", "David", "Mike", "Yoon"]

for i, name in enumerate(names):
    print(name, f"lieks color {colors[i]}")

