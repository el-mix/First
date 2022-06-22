import random


ran_nub = random.randint(1,100)
while True:
    int_user1 = input("Введите целое число: ")
    int_user = int(int_user1)
    if  not int_user1.isdigit():
        print ("Введите целое число: ")


    if int_user > ran_nub:
        print("Загаданное число меньше.")
    elif int_user < ran_nub:
        print("Загаданное число больше.")
    elif int_user == ran_nub:
        print("Ура!!! Вы отгадали это число.")
        print("Желаете еще сыграть? д\н : ")
        user = input()
        if user != "д":
            Print("До скорых встреч")
            break
        else:
            continue
