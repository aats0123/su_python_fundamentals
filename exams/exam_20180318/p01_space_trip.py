destination = input()
distance = int(input())
budget = int(input())
consumption = float(input())
gas_price = float(input())

expenses = (distance / 100) * consumption * gas_price

if budget >= expenses:
    print(f'Off to {destination} with ${(budget - expenses):.2f} for snacks')
else:
    print(f'Maybe another time, need ${(expenses - budget):.2f} more')