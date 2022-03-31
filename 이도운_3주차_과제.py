# 문제 1번
def question1():
    # your code
    return "next"

# 문제 2번
def leapYear(year):
    # your code
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 ==0:
                return "윤년입니다"
            else:
                return "윤년이 아닙니다"
        else:
            return "윤년입니다"
    else:
        return "윤년이 아닙니다"        

# 문제 3번
def alram(time):
    # your code
    hour = int(time // 100)
    minute = int(time % 100)
    if minute <45:
        hour = hour - 1
        minute = minute +15
    elif 45 <= minute <= 59:
        minute = minute - 45
    else:
        return "Error"
    if 1045 <= time <= 1244:
        return "오전" + str(hour) + "시" + str(minute) + "분"
    elif 000 <= time <= 1044:
        return "오전" + str(hour) + "시" + str(minute) + "분"
    elif 1245 <= time <= 2444:
        return "오후" + str(hour) + "시" + str(minute) + "분"
    else:
        return "Error"

# 문제 4번
def findDaesun(x1,y1,r1,x2,y2,r2):
    # your code
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            return "어딘지 모르겠다 오바"
        else:
            return 0
    else:
        if r1 + r2 < distance or r1 > distance + r2 or r2 > distance + r1:
            return 0
        elif r1 +r2 == distance or r1 == distance + r2 or r1 == distance + r2:
            return 1
        else:
            return 2 