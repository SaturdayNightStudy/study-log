# Python

## Python의 특징

- 인터프리터 기반의 객체지향 언어
- 플랫폼에 구애받지 않는 언어
- 동적 타이핑 방식의 언어
- 리플렉션을 지원하는 언어
- 확장성이 뛰어난 언어

## 자료형

### Number(숫자 자료형)

```python
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(2*(3+1))
```

### String(문자열 자료형)

```python
test = "Hello World!"

test = 'Hello World!'

# r’’ 로 문자열을 감싸주게 되면 raw라는 뜻으로 아무 의미없는 문자열이라는 것을 나타냄.
test = r'C:\Test'

first = 'Ji'
last = 'Ny'

print(first + last)  # JiNy
print(last * 5)      # NyNyNyNyNy
```

### Boolean(논리 자료형)

```python
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not 5 > 10)
```

### 변수

```python
animal = "강아지"
name = "연탄이"
age = 4
hobby = "낮잠"
is_adult = age >= 3

print("우리집" + animal + "의 이름은 " + name + "에요.")
print(name + "는 " + str(age) + "살이며, " + hobby + "를 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))
```

- 숫자를 문자로 변환하지 않으면 아래와 같은 에러가 발생함

```txt
예외가 발생했습니다. TypeError
can only concatenate str (not "bool") to str
```

### 주석

```python
# 문장 하나 주석

'''
여러
문장
주석
'''
```

## 연산자

### 연산자

```python
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
```

### 숫자처리함수

```python
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
```

### 랜덤 함수

```python
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
```

## 문자열 처리

### 문자열

```python
sentence = '나는 소년입니다'
sentence2 = "파이썬은 쉬워요"
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)
```

### 슬라이싱

```python
jumin = "990120-1234567"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])
print("생년월일 : " + jumin[:6])
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리 : " + jumin[-7:])

```

# Reference

[파이썬 강의(기본편)]() <br/>
[Myungseo Kang](https://blog.myungseokang.dev/posts/python-basic-grammar1/)
