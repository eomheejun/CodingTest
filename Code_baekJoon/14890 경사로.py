def hor(idx):
    global res
    # 현재 높이
    temp = board[idx][0]
    # 경사로 놓을 수 있는지 확인하기 위한 용도
    temp_len = 1
    # 한 칸 내려갈 때, 경사로를 놓을 수 있는 충분한 길이 있는지 확인
    check = 0
    # 끝까지 도달했는지 확인 용도
    cnt = 1
    for w in range(1, N):
        if check == 0:
            # 높이 같으면
            if board[idx][w] == temp:
                temp_len += 1
                cnt += 1
            # 현재 높이가 직전 높이 +1 일때
            elif board[idx][w] - 1 == temp:
                # 경사로를 놓을 충분한 공간이 있는지 확인
                if temp_len >= L:
                    # 초기화
                    temp_len = 1

                    # 높이 변경
                    temp = board[idx][w]
                    cnt += 1
                else:
                    break
            # 현재 높이가 직전 높이 -1 일때
            elif board[idx][w] + 1 == temp:
                # 남은 길이가 경사로의 길이 이상인지 확인
                if N - w >= L:
                    temp_len = 0
                    temp = board[idx][w]
                    # 현재 위치도 포함하기 때문에 경사로 길이에서 -1 해주기
                    check = L - 1
                    cnt += 1
                else:
                    break
            else:
                break
        else:
            # 경사로 놓을 충분한 공간 확인
            if board[idx][w] == temp:
                check -= 1
                cnt += 1
            else:
                break
    if cnt == N:
        res += 1
    return

def ver(idx):
    global res
    temp = board[0][idx]
    temp_len = 1
    check = 0
    cnt = 1
    for w in range(1, N):
        if check == 0:
            if board[w][idx] == temp:
                temp_len += 1
                cnt += 1
            elif board[w][idx] - 1 == temp:
                if temp_len >= L:
                    temp_len = 1
                    temp = board[w][idx]
                    cnt += 1
                else:
                    break
            elif board[w][idx] + 1 == temp:
                if N - w >= L:
                    temp_len = 0
                    temp = board[w][idx]
                    check = L - 1
                    cnt += 1
                else:
                    break
            else:
                break
        else:
            if board[w][idx] == temp:
                check -= 1
                cnt += 1
            else:
                break
    if cnt == N:
        res += 1
    return

# N, L
N, L = map(int, input().split())
# 지도
board = [list(map(int, input().split())) for _ in range(N)]
# 길의 개수
res = 0
for q in range(N):
    hor(q)
    ver(q)
print(res)