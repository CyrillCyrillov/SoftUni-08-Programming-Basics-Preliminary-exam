target = float(input())

next_cocktail = " "
quantity = 0
sum = 0

while next_cocktail != "Party!" and sum <= target:
    next_cocktail = input()
    if next_cocktail != "Party!":
        quantity = int(input())
        price = quantity * len(next_cocktail)
        if price % 2 != 0:
            price = price * 0.75
        sum += price

if sum >= target:
    print("Target acquired.")
else:
    print(f"We need {target - sum:.2f} leva more.")
print(f"Club income - {sum:.2f} leva.")
