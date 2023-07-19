# string에서 특정 문자열 바꾸기
sentence = "Dog is love"
print(sentence[-4:])
print(sentence[7:])

# string에서 특정 문자열 바꿔서 출력하기
sentence.replace("Dog", "Cat")

# string의 길이를 구하고 중복되는 문자의 갯수 출력하기
txt = "lalalalalalalalalala"
print(len(txt))
print(txt.count("a"))

# string에서 특정 문자를 제거하고 출력하기
phone_number = "010-1234-5678"
phone_number.replace("-"," ")

" ".join(phone_number.split("-"))

# 문자열 출력하기
a = "hello"
b = "python"
print(a + "! " + b)

# 리스트에서 특정 문자를 제거하고 출력하기
color = ["red", "pink", "orange", "yellow", "green",
          "blue", "purple", "black", "white"]

color.pop(4)
print(color)

color.remove("green")
print(color)

# 리스트 항목에 특정 문자를 추가하고 출력하기
color = ["red", "orange", "yellow", "green",
          "blue", "purple", "black", "white"]

color.insert(1, "pink")
print(color)

# 딕셔너리 a에서 B에 해당하는 값을 출력하기
a = {'A':90, 'B':80, 'C':70, 'D':60}
a.get("B")