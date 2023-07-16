# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print


year = int(input("введит год который будем проверять: "))
MAIN_LEAP_CRYTERIA = 4
ADDITIONAL_LEAP_CRYTERIA = 400
LEAP_EXCLUDINGG_CRYTERIA = 100

if year % MAIN_LEAP_CRYTERIA == 0 and year%LEAP_EXCLUDINGG_CRYTERIA !=0 or year %ADDITIONAL_LEAP_CRYTERIA == 0:
    print ("Год высокосный")
else: print ("Год обычный")
