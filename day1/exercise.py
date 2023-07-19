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

# 문자열 출력하기
a = "hello"
b = "python"
print(a + "! " + b)