# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 18:49:11 2022

@author: tjwjd
"""

# 함수
def add(a,b):
    return a + b

print(add(3,7))

print(add(b=3, a=7))

#%%
# 함수 안에서 함수 밖의 변수 데이터를 변경해야 하는 경우가 있다.
# 이때 함수에서는 global 키워드로 변수를 지정하면, 
# 해당 함수 에서는 지역 변수를 만들지 않고, 함수 바깥에 선언된 변수를 바로 참조하게 된다.

a = 0

def func():
    global a
    a += 1
    
for i in range(10):
    func()
    
print(a)

#%%
def add(a,b):
    return a + b

# 일반적인 add() 메서드 사용
print(add(3, 7))

# 람다 표현식으로 구현한 add() 메서드
print((lambda a,b: a+b)(3,7))











