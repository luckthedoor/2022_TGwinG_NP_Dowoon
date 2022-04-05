# your code 부분에 코딩하여 문제를 풀이해주세요.
# print 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 4주차 과제에는 출력을 요구하는 문제가 없습니다.
# input 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 4주차 과제에는 입력을 요구하는 문제가 없습니다.
# answer 변수를 사용하여 문제를 풀이하세요. 반환값은 answer 변수입니다.
# 함수 내에서 컴파일 에러, 런타임 에러가 발생하면 해당 문제 점수 0점 처리하겠습니다.
# 함수명 변경하지 마세요. 변경 시 해당 문제 점수 0점 처리하겠습니다.
# 제출 기한: 2022년 4월 5일 23시 59분.
# 지각 제출 기한: 2022년 4월 6일 23시 59분. 주차 점수에서 20% 감점

# 문제 1번
def intervention(queue):
    answer = list()
    # your code
    queue5 = list(queue[:5])
    if "성은" in queue:
        if "성은" in queue5:
            queue.append("승호")
            answer = queue
        else:
            queue.insert(int(queue.index("성은"))+1,"승호")
            answer = queue
    else:
        queue.append("승호")
        answer = queue
    return answer

# 문제 2번
def pascal(n):
    answer = list()
    # your code
    pascallist = []
    for i in range(n):
        pascallist.append([])
        pascallist[i].append(1)
        for j in range(1,i):
            pascallist[i].append(pascallist[i-1][j-1]+pascallist[i-1][j])
        
        if n != 0:
            pascallist[i].append(1)

    answer = pascallist[n-1]
    return answer


# 문제 3번
def auto_complete(entry, searchWords):
    answer = list()
    # your code
    Searchwords = []
    for i in searchWords:
        if entry in i:
            Searchwords.append(i)
    
    answer = Searchwords
    return answer

# 문제 4번
def stock_price(stockChart):
    answer = str()
    # your code
    recentstockChart = []
    for i in stockChart:
        recentstockChart.append(i)

    income = sum(recentstockChart[:i+1])

    if income > 0:
        answer = "%d일 전에 샀어야지 으이구"
    else:
        answer = "아니야 조금만 더 기다려"
    return answer

# 문제 5번
def decryption(letter):
    answer = str()
    # your code
    abclist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    decodelist = ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c']
    decoding = []

    for i in letter:
        if abclist in list(letter):
            decoding.append(decodelist[abclist.index(i)])
        else:
            decoding.append(i)
    
    answer = decoding

    return answer