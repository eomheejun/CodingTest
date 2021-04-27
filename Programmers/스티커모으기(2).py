def solution(sticker):
    if len(sticker)<=2:
        if len(sticker) == 1:
            return sticker[0]
        else:
            return max(sticker[0],sticker[1])
    else:
        first = [0] * (len(sticker))
        second = [0] * (len(sticker))

        first[0] = sticker[0]
        first[1] = sticker[0]
        second[0] = 0
        second[1] = sticker[1]

        for i in range(2, len(sticker)-1):
            first[i] = max(first[i - 2] + sticker[i], first[i - 1])
        for i in range(2, len(sticker)):
            second[i] = max(second[i - 2] + sticker[i], second[i - 1])

        return max(max(first),max(second))

sticker=[14, 6, 5, 11, 3, 9, 2, 10]

print(solution(sticker))