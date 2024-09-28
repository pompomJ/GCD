# 2つの数字の最大公約数を求める
def gcd(x, y):
    x_list = []
    y_list = []
    
    cnt = 1
    while x > cnt:
        if x % cnt == 0:
            x_list.append(cnt)
        cnt += 1

    cnt = 1
    while y > cnt:
        if y % cnt == 0:
            y_list.append(cnt)
        cnt += 1

    cnt_x, cnt_y = 0, 0
    gcd_list = []
    for cnt_x in x_list:
        for  cnt_y in y_list:
            if cnt_x == cnt_y:
                gcd_list.append(cnt_y)

    return max(gcd_list)

print(gcd(44, 72))
