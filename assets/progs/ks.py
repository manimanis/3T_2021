t = int(input())

w1 = "KICK"
w2 = "START"

for i in range(1, t+1):
    s = input()
    kc = 0
    tc = 0
    j = 0
    ls = len(s)
    while j < ls:
        if s[j] == 'K':
            k = 0
            while k < len(w1) and j+k < ls and s[j+k] == w1[k]:
                k += 1
            if k == len(w1):
                kc += 1
                j += k-1
            else:
                j += 1
        elif s[j] == 'S':
            k = 0
            while k < len(w2) and j+k < ls and s[j+k] == w2[k]:
                k += 1
            if k == len(w2):
                tc += kc
                j += k
            else:
                j += 1
        else:
            j += 1
    print(f'Case #{i}: {tc}')