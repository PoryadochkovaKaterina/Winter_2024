class Menu:
    def __init__(self, spisok):
        self.spisok = spisok   # меню в виде словаря
    def info(self):   # вывод меню
        for i in self.spisok:
            print(f'{i}: {self.spisok[i]}')
    def menu_сhoice(self, choice):   # выбор из меню
        for i in self.spisok:
            # print(f'{i}: {self.spisok[i]}')
            if i == choice:
                product = self.spisok[choice]
                return product
            else: pass
        print('Такого товара нет')
        return 0

class Buyer:
    def __init__(self, name, cash, balance):   # покупатель с количеством денег
        self.cash = cash   # количество наличных
        self.balance = balance   # количество на карте
        self.name = name

    def wallet(self):   # оплата
        choice_wallet = input('Как будете платить, наличными или картой? ').lower()
        if choice_wallet == 'картой':
            buyer_Petr.give_monye_balance(price_basket)
        elif choice_wallet == 'наличными':
            buyer_Petr.give_money_cash(price_basket, int(input('Введите сумму: ')))
        else:
            print('Такого способа оплаты нет!')
            yes_no = input('Желаете продолжить? ').lower()
            if yes_no == 'да':
                buyer_Petr.wallet()
            else:
                pass

    def give_money_cash(self, money, summa):   # money - сколько стоит товар, summa - сколько дает покупатель
        if summa >= money:   # проверка на то, хватит ли денег на оплату наличными
            change = summa - money
            self.cash = (self.cash - summa) + change
            print(f'Оплата прошла. Ваша сдача: {change}. Остаток: {self.cash}')

        else:
            print(f'Недостаточно средств. Цена: {money}, дано: {summa}')
            yes_no = input('Желаете продолжить? ').lower()
            if yes_no == 'да':
                buyer_Petr.wallet()
            else:
                pass

    def give_monye_balance(self, money):
        if self.balance >= money:   # проверка на то, хватит ли денег на оплату по карте
            self.balance -= money
            print(f'Оплата прошла. Остаток на карте: {self.balance}')
        else:
            print('Недостаточно средств. Остаток на карте: {self.balance}')
            yes_no = input('Желаете продолжить? ').lower()
            if yes_no == 'да':
                buyer_Petr.wallet()
            else:
                pass


print('Меню заведения: ')
menu = Menu({'латте': 99,
             'чай черный': 45,
             'капучино': 108,
             'какао': 75,
             'американо': 85,
             'слойка': 60,
             'пироженное': 123,
             'сэндвич': 119,
             'рулет': 54,
             'круассан': 195})
menu.info()
print()

buyer_Petr = Buyer('Петр', 1500, 2000)

cou = 0
res = []
n = int(input('Сколько раз в неделю ходите в заведение: '))
for i in range(1, n+1):
    print(f'День {i}')
    basket = ''
    price_bas = []
    price_basket = []
    s = 0
    while True:
        print('Выберете товар: ')
        choice = input().lower()
        price = menu.menu_сhoice(choice)

        price_bas.append(price)

        print(f'Желаете что-то еще? Да/Нет')
        yes_no = input().lower()
        if yes_no == 'да':
            continue
        else:
            break

    price_basket = sum(price_bas)
    res.append(price_basket)
    print(f'Сумма заказа: {price_basket}')

    buyer_Petr.wallet()

print()
print(f'Вы посетиле заведение {n} раз, потратили {sum(res)} денег')
