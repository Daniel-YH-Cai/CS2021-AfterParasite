def asteroid(str):
    list = aggregate(str)
    score = 0
    origin = 0
    for i in range(len(list)):
        l = i
        r = i
        tempScore = 0
        while l >= 0 and r < len(list) and list[l]['char'] == list[r]['char']:
            if l == r:
                tempScore += calculateScore(list[l]['num'])
            else:
                tempScore += calculateScore(list[l]['num'] + list[r]['num'])
            l -= 1
            r += 1
        if tempScore > score:
            score = tempScore
            origin = list[i]['index'] + int(list[i]['num'] / 2)
    return origin, score


def aggregate(str):
    list = []
    l = 0
    num = 0
    for i in range(len(str)):
        if str[i] != str[l]:
            list.append({'char': str[l], 'num': num, 'index': l})
            l = i
            num = 1
        else:
            num += 1
    list.append({'char': str[l], 'num': num, 'index': l})
    return list


def calculateScore(n):
    if n > 0 and n <= 6:
        return n
    elif n >= 7 and n < 10:
        return 1.5 * n
    elif n >= 10:
        return 2 * n


def main():
    test1 = "CCAAABBBAAACCCB"
    test2 = "CCAAABBAAACCCB"
    test3 = "CCCAAABBBAAACCC"
    test4 = "BBAAABBB"
    test5 = "CCCAAAAABBBAAACCC"
    print(asteroid(test1))
    print(asteroid(test2))
    print(asteroid(test3))
    print(asteroid(test4))
    print(asteroid(test5))

if __name__ == '__main__':
    main()
