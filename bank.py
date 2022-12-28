"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
def bank_account():
    b_sum = 0
    history = []

    def buy(b_sum):
        cost = int(input("Введите сумму покупки: "))
        if cost > b_sum:
            print("Недостаточно средств")
        else:
            b_sum -= cost
            name = input("Введите наименование покупки: ")
            history.append((name, cost))
        return b_sum

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        print(f"Ваш текущий счет: {b_sum}")
        choice = input('Выберите пункт меню: ')
        if choice == '1':
            cost = int(input("Введите сумму пополнения: "))
            b_sum += cost
        elif choice == '2':
            b_sum = buy(b_sum)
            # cost = int(input("Введите сумму покупки: "))
            # if cost > b_sum:
            #     print("Недостаточно средств")
            # else:
            #     b_sum -= cost
            #     name = input("Введите наименование покупки: ")
            #     history.append((name, cost))
        elif choice == '3':
            print(history)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')
