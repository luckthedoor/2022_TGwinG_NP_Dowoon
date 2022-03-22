# 문제 1번
def sum(a,b):
    # your code
    return a+b

# 문제 2번
def sub(a,b):
    # your code
    return a-b

# 문제 3번
def mul(a,b):
    # your code
    return a*b

# 문제 4번
def div(a,b):
    # your code
    return a/b

# 문제 5번
def distance(x1,y1,x2,y2):
    # your code
    return ((x1-x2)**2 + (y1-y2)**2)**1/2

# 문제 6번
def short():
    lylic = "life is short art is long"
    # your code
    return lylic[8:13]

# 문제 7번
def myReverse(string):
    # your code
    newString = string[::-1]
    return(newString)

# 문제 8번
def letMeIntroduceMyself():
    # your code
    name = input("이름을 입력하시오: ")
    hobby = input("취미를 입력하시오: ")
    univ = input("재학 중인 대학교를 입력하시오: ")
    birthday = input("생일을 입력하시오(예시: 020508): ")
    month = birthday[2:4]
    day = birthday[4:6]
    return ("제 이름은 {0}입니다. 제 취미는 {1}이구요. 저는 {2}를 다니고 있습니다.제 생일은 {3}월 {4}일 입니다.").format(name, hobby, univ, month, day) 

# 문제 9번
def calcAI():
    # your code
    a = int(input("Enter 'a' as integer number: "))
    b = int(input("Enter 'b' as integer number: "))
    Sum = a + b
    return ("두 수의 합은 {0}입니다.").format(Sum)