# 구구단
def gugudan():
    for i in range(2, 10):
        print(f'* {i}단 *')
        for j in range(1, 10):
            print(f'{i} * {j} = {i * j}')

gugudan()

# 커피 자판기
def cafe(money, coffe): 
    manu = {"americano":2500}
    for name, pay in manu.items():
        if str(coffe) == name:
            print(f"커피는 {pay}원 입니다.")
            result = money - pay
    print(f'커피 나왔습니다! 거스름돈은 {result}원 입니다')

cafe(10000, "americano")

# 체질량 지수
def bmi(weight, height):
    value = weight / (height)**2
    if value < 18.5:
        print("저체중입니다")
    elif value >= 18.5 and value < 25:
        print("정상체중입니다")
    elif value >= 25 and value < 30:
        print("과체중입니다")
    else:
        print("비만입니다.")

bmi()



