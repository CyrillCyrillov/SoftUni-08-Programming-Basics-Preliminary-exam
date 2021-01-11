nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

sum = ((((nylon + 2) * 1.5) + (paint * 1.1 * 14.50) + (thinner * 5) + 0.4) * 0.3 * hours) + (((nylon + 2) * 1.5) + (paint * 1.1 * 14.50) + (thinner * 5) + 0.4)

print(f"Total expenses: {sum:.2f} lv.")
