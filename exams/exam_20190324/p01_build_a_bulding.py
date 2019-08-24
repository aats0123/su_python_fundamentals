budget = float(input())
capital = float(input())
number_of_investors = int(input())
output = ''
for count in range(1, number_of_investors + 1):
    money = float(input())
    capital += money
    output += f'\nInvestor {count} gave us {money:.2f}.'
    if capital >= budget:
        extra_money = capital - budget
        output += f'\nWe will manage to build it. Start now! Extra money - {extra_money:.2f}.'
        break
output = output.lstrip('\n')
if capital < budget:
    output += f'\nProject can not start. We need {(budget - capital):.2f} more.'
print(output)

