﻿a = int (input ('Введите трехзначное число'))
if a > 100 and a < 999:
    b = a % 10
    c = (a // 10) % 10
    d = a // 100
    print (b + c + d)
else:
    print ('Вы ввели не трехзначное число')