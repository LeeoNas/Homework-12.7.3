per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = int(input("Введите сумму, которую планируете положить под проценты: "))

deposit = [
    int(money * per_cent['ТКБ'] / 100),
    int(money * per_cent['СКБ'] / 100),
    int(money * per_cent['ВТБ'] / 100),
    int(money * per_cent['СБЕР'] / 100)
]

print("Накопленные средства за год вклада в каждом из банков:", deposit)

max_deposit = max(deposit)

print("Максимальная сумма, которую вы можете заработать — {}".format(max_deposit))

