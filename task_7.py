# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

num = int(input("введите число: "))
if num >=1 and num <10:
    res = num ** 2
    message = "Цифра"
elif num >=11 and num <100:
    res = (num//10) + (num%10)
    message = "двухзначное число"
elif num >=100 and num <1000:
    res = ((num%10)*100) + ((num%100-num%10))+(num//100)
    message = "трехзначное число"
print(message)
print(res)