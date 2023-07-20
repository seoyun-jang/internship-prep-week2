# # 구구단
# def gugudan():
#     for i in range(2, 10):
#         print(f'* {i}단 *')
#         for j in range(1, 10):
#             print(f'{i} * {j} = {i * j}')

# gugudan()

# # 커피 자판기
# def cafe(money, coffee): 
#     manu = {"americano":2500}
#     for name, pay in manu.items():
#         if str(coffee) == name:
#             print(f"커피는 {pay}원 입니다.")
#             result = money - pay
#     print(f'커피 나왔습니다! 거스름돈은 {result}원 입니다')

# cafe(10000, "americano")


coffee_dictionary = {
    "americano" : {
        "price": 2000,
        "type" : "ice"
    },
    "latte" : {
        "price": 3000,
        "type" : "ice"
    }
}

def vending_machine():
    amount = int(input("가격을 입력해주세요: "))
    coffee = input("커피를 주문해주세요: ")

    if coffee_dictionary.get(coffee):
        coffee_info = coffee_dictionary[coffee]
        price = coffee_info['price']
        if (amount >= price):
            print(f"거스름돈은 {amount - price} 입니다")
        else:
            print("잔액이 부족합니다")

    else:
        print("해당 메뉴는 존재하지 않습니다")

vending_machine()



# # 체질량 지수
# def bmi(weight, height):
#     value = round(weight / (height * 0.01)**2 , 2)
#     print(f'BMI지수는 {value}로')
#     if value < 18.5:
#         print("저체중입니다")
#     elif value < 25:
#         print("정상체중입니다")
#     elif value < 30:
#         print("과체중입니다")
#     else:
#         print("비만입니다.")

# bmi(55, 164)



