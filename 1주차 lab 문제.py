Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:/Users/정가은/OneDrive/바탕 화면/circle.py
원의 반지름 4.0
원의 면적 50.24
원의 둘레 25.12
print('hello python!!')
hello python!!

============ RESTART: C:/Users/정가은/OneDrive/바탕 화면/circle_with_var.py ===========
원의 반지름 4.0
원의 면적 50.24
원의 둘레 25.12

============ RESTART: C:/Users/정가은/OneDrive/바탕 화면/circle_with_var.py ===========
원의 반지름 6.0
원의 면적 113.03999999999999
원의 둘레 37.68
name=전우치
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    name=전우치
NameError: name '전우치' is not defined
name='전우치'
print('나의 이름은:', name)
나의 이름은: 전우치
age=27
print('나의 나이는:',age)
나의 나이는: 27
height = 179
print('나의 키는', height, 'cm입니다.')
나의 키는 179 cm입니다.
sum = 10+20
print('10+20=', sum)
10+20= 30
mult = 10*20
print('10*20=', mult)
10*20= 200

================= RESTART: C:/Users/정가은/OneDrive/바탕 화면/변수테스트.py ================
안녕 나는 홍길동 이야. 나는 나이가 27 살이야.
4 + 10
14
4.0 - 0.1
3.9
20*20
400
11/2
5.5
11//2
5
11%2
1
4 ** 5
1024
123*123
15129
1357+2468
3825
5 **4
625
10/4
2.5
10//5
2
10%5
0
5%2
1
2**0.5
1.4142135623730951

================= RESTART: C:/Users/정가은/OneDrive/바탕 화면/변수테스트.py ================
23 178.5
num = 85
type(num)
<class 'int'>
pi = 3.14159
type(pi)
<class 'float'>
message="good"
type(message)
<class 'str'>
foo=100
type(foo)
<class 'int'>
foo='hello'
type(foo)
<class 'str'>
l=[100,300,500,900]
type(l)
<class 'list'>
d={'apple': 3000, 'banana': 4200}
type(d)
<class 'dict'>
t=('홍길동', 30, '율도국왕')
type(t)
<class 'tuple'>
str(100)
'100'
str(12.3)
'12.3'
x=['A','B','C']
str(x)
"['A', 'B', 'C']"
x=["a","b","c"]
str(x)
"['a', 'b', 'c']"
txt1='강아지 이름은 "햇님"임'
txt1
'강아지 이름은 "햇님"임'
txt3="친구가 |"햇님이좋아!|"라고 말햇다"
SyntaxError: invalid syntax
txt3
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    txt3
NameError: name 'txt3' is not defined. Did you mean: 'txt1'?
>>> txt3="친구가 \n"햇님이좋아!\n"라고 말햇다"
SyntaxError: invalid syntax
>>> a=8+2i
SyntaxError: invalid decimal literal
>>> a=8+2j
>>> b=4+3j
>>> a+b
(12+5j)
>>> a-b
(4-1j)
>>> a*b
(26+32j)
>>> a/b
(1.52-0.64j)
>>> a=1024
>>> a>>1
512
>>> a>>2
256
>>> a=a>>1
>>> a
512
>>> a=1
>>> a<<1
2
>>> name=input('이름을 입력하세요:')
이름을 입력하세요:김유신
>>> print(name,'님이 입장하셨습니다.')
김유신 님이 입장하셨습니다.
>>> m=int(input('숫자m을 입력하세요:'))
숫자m을 입력하세요:30
>>> n=int(input('숫자n을 입력하세요:'))
숫자n을 입력하세요:50
>>> print('m+n=', m+n)
m+n= 80
>>> print('m-n+', m-n)
m-n+ -20
