import random
def igra():
    print("67Игра67: угадай число")
    print("загаданное число от 1 до 1000")
    rannum=random.randint(1, 1000)
    popitki=0
    while True:
        try:
            gues=input("Введите число или стоп для выхода: ")
            if gues.lower()=='стоп':
                print("Загаданное число было:", rannum)
                break
            prinimatel=int(gues)
            popitki+=1
            raznica=abs(rannum-prinimatel)
            if prinimatel==rannum:
                print(f"ВЫ ОТГАДАЛИ ЙОУ!!!! Вы угадали за {popitki} попыток. Я бы лучше сделал.")
                break
            elif prinimatel==67:
                print("Хахахаха! Это же сиксеееееевен!")
            elif raznica>100:
                print("Очень холодно")
            elif raznica>10:
                print("Холодно")
            else:
                print("близко")
        except ValueError:
            print("Ты угараешь?")
igra()