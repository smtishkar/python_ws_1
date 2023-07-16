# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

num = 1

for i in range (1,9):
    num +=1
    print("-"*20)
    for j in range (2,11):
        res=num*j
        print(num, "*", j, "=", res)
    print("       ".join(4))