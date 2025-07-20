import sys

def card(N, M, cardList):
    resultGap = list()
    for i in range(N):
        cardM = M
        result = 0
        if cardM - cardList[i] > 0:
            cardM -= cardList[i]
            result += cardList[i]
            for j in range(i+1, N):
                if cardM - cardList[j] > 0:
                    cardM -= cardList[j]
                    result += cardList[j]
                    for k in range(j+1, N):
                            if cardM - cardList[k] > 0:
                                resultGap.append(result + cardList[k])
                            elif cardM - cardList[k] == 0:
                                return M
                            else:
                                continue
                else:
                    continue
                cardM += cardList[j]
                result -= cardList[j]
        else:
            continue
        cardM += cardList[i]
        result -= cardList[i]
    return max(resultGap)

N, M = map(int, input().split())
cardList = list(map(int, sys.stdin.readline().rstrip().split()))

print(card(N, M, cardList))