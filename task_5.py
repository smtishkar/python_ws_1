# Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
# Используйте while и if.
# Попробуйте разные значения e и n.

n = int(input("Введите число: "))
# n =16
e = 3
num = 1
sum = 0
while num < n:
    num+=1
    if num % 2 == 0 and num % e !=0:
        sum += num
print (sum)