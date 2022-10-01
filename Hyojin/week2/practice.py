# 주석 처리
'''
# 자료형
# 숫자
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(2*(3+1))

# 문자열
print('풍선')

# 논리형
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not 5 > 10)

# 변수
animal = "강아지"
name = "연탄이"
age = 4
hobby = "낮잠"
is_adult = age >= 3

print("우리집" + animal + "의 이름은 " + name + "에요.")
print(name + "는 " + str(age) + "살이며, " + hobby + "를 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))

# 연산자
print(5 + 6)   # 11
print(5 - 2)    # 3
print(3 * 8)   # 24
print(3 ** 3)  # 27, 제곱
print(8 / 2)    # 4.0, float형
print(8 // 2)   # 4, int형
print(8 % 3)   # 2, 나머지

# 연산자
print(5 + 6)   # 11
print(5 - 2)    # 3
print(3 * 8)   # 24
print(3 ** 3)  # 27, 제곱
print(8 / 2)    # 4.0, float형
print(8 // 2)   # 4, 몫 구하기, int형
print(8 % 3)   # 2, 나머지 구하기

print(10 > 3)
print(4 >= 7)
print(10 < 3)
print(5 <= 5)
print(3 == 3)
print(4 == 2)
print(3 + 4 == 7)

print(1 != 3)
print(not (1 == 3))

print((3 > 0) and (3 < 5))
print((3 > 0) & (3 > 5))
print((3 > 0) or (3 < 5))
print((3 > 0) | (3 > 5))
print((3 < 0) | (3 > 5))

# 숫자처리함수
from math import *

print(abs(-5))  # 5
print(pow(4, 2))  # 4^2 = 16
print(max(5, 12))  # 12
print(min(5, 12))  # 5

print(round(3.14))  # 3
print(round(4.99))  # 5

print(floor(4.99))  # 내림, 4
print(ceil(3.14))  # 올림, 4
print(sqrt(16))  # 제곱근, 4

# 랜덤 함수
from random import *
print(random())  # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10)    # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10))  # 0 ~ 10 미만의 임의의 값 생성

print()
print(int(random() * 10) + 1)  # 1~ 10 이하의 임의의 값 생성
print(int(random() * 10) + 1)  # 1~ 10 이하의 임의의 값 생성
print(int(random() * 10) + 1)  # 1~ 10 이하의 임의의 값 생성
print(int(random() * 10) + 1)  # 1~ 10 이하의 임의의 값 생성
print(int(random() * 10) + 1)  # 1~ 10 이하의 임의의 값 생성

# 랜덤 함수
from random import *
print(random())  # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10)    # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10))  # 0 ~ 10 미만의 임의의 값 생성

print()
print(int(random() * 10) + 1)  # 1~ 10 이하의 임의의 값 생성
print(int(random() * 10) + 1)  # 1~ 10 이하의 임의의 값 생성
print(int(random() * 10) + 1)  # 1~ 10 이하의 임의의 값 생성
print(int(random() * 10) + 1)  # 1~ 10 이하의 임의의 값 생성
print(int(random() * 10) + 1)  # 1~ 10 이하의 임의의 값 생성
print()
print(randrange(1, 45))  # 1 ~ 45 미만의 임의의 값 생성

# 랜덤 함수
from random import *
print(random())  # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10)    # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10))  # 0 ~ 10 미만의 임의의 값 생성

print()
print(int(random() * 10) + 1)  # 1~ 10 이하의 임의의 값 생성
print(int(random() * 10) + 1)  # 1~ 10 이하의 임의의 값 생성
print(int(random() * 10) + 1)  # 1~ 10 이하의 임의의 값 생성
print(int(random() * 10) + 1)  # 1~ 10 이하의 임의의 값 생성
print(int(random() * 10) + 1)  # 1~ 10 이하의 임의의 값 생성
print()
print(randrange(1, 45))  # 1 ~ 45 미만의 임의의 값 생성
print(randint(1, 45))   # 1 ~ 45 이하의 임의의 값 생성

### 문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

# 슬라이싱
jumin = "990120-1234567"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])
print("생년월일 : " + jumin[:6])
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리 : " + jumin[-7:])

# 문자열처리함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper)  # 대문자인가 ? True : False
print(len(python))  # 문자열 길이
print(python.replace("Python", "Jave"))  # Jave is Amazing

index = python.index("n")   # 문자 위치 찾기
print(index)
index = python.index("n", index + 1)    # 두번째 위치
print(index)

print(python.find("n"))
print(python.find("Jave"))  # 값이 없을 경우 -1 반환
# print(python.index("Jave")) # 값이 없을 경우 오류 반환 -> 프로그램 종료

print(python.count("n")) # 2

'''

# Test
