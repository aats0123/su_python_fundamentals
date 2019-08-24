lost_fights = int(input())
helmet_price = float(input())
sward_price = float(input())
shield_price = float(input())
armor_price = float(input())
shield_repair_counter = 0
expenses = 0.0

helmet_repairs = lost_fights // 2
sward_repairs = lost_fights // 3
shield_repairs = lost_fights // 6
armor_repairs = shield_repairs // 2

expenses = helmet_repairs * helmet_price + sward_repairs * sward_price + shield_repairs * shield_price + armor_repairs * armor_price


print(f'Gladiator expenses: {expenses:.2f} aureus')

