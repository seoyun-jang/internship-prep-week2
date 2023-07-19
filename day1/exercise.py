# # string에서 특정 문자열 바꾸기
# sentence = "Dog is love"
# print(sentence[-4:])
# print(sentence[7:])

# # string에서 특정 문자열 바꿔서 출력하기
# sentence.replace("Dog", "Cat")

# # string의 길이를 구하고 중복되는 문자의 갯수 출력하기
# txt = "lalalalalalalalalala"
# print(len(txt))
# print(txt.count("a"))

# # string에서 특정 문자를 제거하고 출력하기
# phone_number = "010-1234-5678"
# phone_number.replace("-"," ")

# " ".join(phone_number.split("-"))

# # 문자열 출력하기
# a = "hello"
# b = "python"
# print(a + "! " + b)

# # 리스트에서 특정 문자를 제거하고 출력하기
# color = ["red", "pink", "orange", "yellow", "green",
#           "blue", "purple", "black", "white"]

# color.pop(4)
# print(color)

# color.remove("green")
# print(color)

# # 리스트 항목에 특정 문자를 추가하고 출력하기
# color = ["red", "orange", "yellow", "green",
#           "blue", "purple", "black", "white"]

# color.insert(1, "pink")
# print(color)

# # 딕셔너리 a에서 B에 해당하는 값을 출력하기
# a = {'A':90, 'B':80, 'C':70, 'D':60}

# print(a["B"])
# print(a.get("B"))

# # 교집합과 차집합 출력하기
# s1 = set([1, 2, 3, 4, 5, 6])
# s2 = set([4, 5, 6, 7, 8, 9])

# print(s1 & s2)
# s1.intersection(s2)

# print(s1 - s2)
# s1.difference(s2)

# # 중복이 없는 리스트로 출력하기
# duplication = [1, 2, 3, 4, 4, 4, 9, 11, 11, 11, 14]
# list(set(duplication))


# # 입력받은 점수가 60점 이상인 경우 pass
# 60보다 낮은 경우 fail

score = input("당신의 점수는 몇 점인가요?")

if (int(score) >= 60):
    print("PASS")
else:
    print("FAIL")