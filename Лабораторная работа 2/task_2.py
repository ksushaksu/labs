salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = 0
month = 0
while month < months:
    money_capital += salary - spend
    spend += spend * increase
    month += 1


print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(-1 * money_capital))
