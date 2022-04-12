# your code 부분에 코딩하여 문제를 풀이해주세요.
# print 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 5주차 과제에는 출력을 요구하는 문제가 없습니다.
# input 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 5주차 과제에는 입력을 요구하는 문제가 없습니다.
# result 변수를 사용하여 문제를 풀이하세요. 반환값은 result 변수입니다.
# 함수 내에서 컴파일 에러, 런타임 에러가 발생하면 해당 문제 점수 0점 처리하겠습니다.
# 함수명 변경하지 마세요. 변경 시 해당 문제 점수 0점 처리하겠습니다.
# 제출 기한: 2022년 4월 12일 23시 59분.
# 지각 제출 기한: 2022년 4월 13일 23시 59분. 주차 점수에서 20% 감점

import math

def calcCircleArea(r):
    result = "%0.2f" % (math.pi * float(r) ** 2)
    '''[2]'''
    return result
def calcLog(a, b):
    if a == "e":
        result = "%0.2f" % math.log(float(b))
    else:
        result = "%0.2f" % (math.log(float(b), float(a)))
    '''[3]'''
    return result
def calcSin(x):
    result = "%0.2f" % float(math.sin(int(x)))
    '''[4]'''
    return result
def calcFactorial(X):
    result = int(math.factorial(int(X)))
    '''[5]'''
    return result
def calcCombination(n, r):
    result = int(math.comb(int(n), int(r)))
    '''[6]'''
    return result

def calculator(order):
    Command = order.split()
    if "원넓이:" in Command:
        r = Command[1]
        answer = calcCircleArea(r)
    elif "로그:" in Command:
        a = Command[1]
        b = Command[2]
        answer = calcLog(a, b)
    elif "사인:" in Command:
        x = Command[1]
        answer = calcSin(x)
    elif "팩토리얼:" in Command:
        X = Command[1]
        answer = calcFactorial(X)
    elif "조합:" in Command:
        n = Command[1]
        r = Command[2]
        answer = calcCombination(n, r)
    '''[1]'''
    return answer