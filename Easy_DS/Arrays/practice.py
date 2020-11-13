sum = 7
a = [10, 3, 5, 7, 2, 8, 9, 6, 1, 4]
a.sort()
c = 0
left = 0
right = len(a)-1
while(True):
    if left >= right:
        break
    if a[left] + a[right] > sum:
        right -= 1
    elif a[left] + a[right] < sum:
        left += 1
    elif a[left] + a[right] == sum:
        c += 1
        left += 1
        right -= 1
print(c)