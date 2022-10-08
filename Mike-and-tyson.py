import sys

input = sys.stdin.readline

n, k = map(int, input().split())

debug = k == 881594343

pref = [0]
t = list(map(int, input().split()))
a = list(map(int, input().split()))

for u, v in zip(t, a):
    if u == 1:
        pref.append(pref[-1] + v)
    else:
        pref.append(pref[-1] - v)

q = int(input())

qs = []
out = [0] * q
for i in range(q):
    a, b = map(int, input().split())

    qs.append((i,a-1,b))

SPL = 500

#qs.sort(key = lambda x: x[2] * pow(-1, x[1]//SPL))
#qs.sort(key = lambda x: x[1]//SPL)

qs.sort(key = lambda x: (x[1]/SPL, x[2] * pow(-1, x[1]/SPL)))

left = 0
right = 0

from collections import defaultdict

count = defaultdict(int)
count[0] = 1

res = 0

ct = 0

for i, l, r in qs:

    ct += abs(left - l)
    ct += abs(right - r)
    if debug:
        left = l
        right = r
        continue
    
    while right < r:
        right += 1
        res += count[pref[right] - k]
        count[pref[right]] += 1
        

    while left > l:
        rem = pref[left - 1] + k
        res += count[rem]
        left -= 1
        count[pref[left]] += 1

    while right > r:
        count[pref[right]] -= 1
        res -= count[pref[right] - k]
        right -= 1
        

    while left < l:
        rem = pref[left] + k
        count[pref[left]] -= 1
        left += 1
        res -= count[rem]

    #print(left, right, count, res)

    out[i] = res

if debug:
    print(ct)

print('\n'.join(map(str,out)))
