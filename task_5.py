n = input('Введите шестизначное число:')
oneNum = int (n[0] + n[1] + n[2])
oneSum = ((oneNum % 10) + ((oneNum // 10) % 10) + (oneNum // 100))
twoNum = int (n[3] + n[4] + n[5])
twoSum = ((twoNum % 10) + ((twoNum // 10) % 10) + (twoNum // 100))
if oneSum == twoSum:
    print('yes')
else:
    print('no')