"""
Напишите программу печатающую скидку на поездку в зависимости от набранных баллов.
Программа должна запрашивать количество набранных баллов и печатать сообщение «Ваша скидка:» и скидку:
— от 0 до 49 баллов — «Скидка 10%»;
— от 50 до 99 баллов — «Скидка 15%»;
— от 100 баллов и выше — «Скидка 20%».

Примечание. Наличие функции является обязательным. Функция должна принимать количество набранных баллов.
"""
def control_rates(points):
    if points >= 0 and points <= 49:
        print('10% -- result')
    elif points >= 50 and points <= 99:
        print('15% -- result')
    else:
        print('20% -- result')
    return points

def control_output():
    control_rates(int(input()))
    

def main():
    control_output()
if __name__ == "__main__":
    main()
