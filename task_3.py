# Вариант 1
# n = input('Введите шестизначное число:')
# oneNum = int (n[0] + n[1] + n[2])
# oneSum = ((oneNum % 10) + ((oneNum // 10) % 10) + (oneNum // 100))
# twoNum = int (n[3] + n[4] + n[5])
# twoSum = ((twoNum % 10) + ((twoNum // 10) % 10) + (twoNum // 100))
# if oneSum == twoSum:
#     print('yes')
# else:
#     print('no')

# Вариант 2
n = input('Введите шестизначное число:')
oneNum = int (n[0] + n[1] + n[2])
oneSum = 0
while oneNum > 0:
    x = oneNum % 10
    oneSum = oneSum + x
    oneNum = oneNum // 10
print (oneSum)

twoNum = int(n[3] + n[4] + n[5])
twoSum = 0
while twoNum > 0:
    x = twoNum % 10
    twoSum = twoSum + x
    twoNum = twoNum // 10
print(twoSum)
if oneSum == twoSum:
    print('yes')
else:
    print('no')