numbers = int(input())
max_point = 0
winner = " "

for i in range(1, numbers + 1):
    sum = 0
    next_name = input()
    next_points = " "
    while next_points != "Stop":
        next_points = input()
        if next_points != "Stop":
            sum += int(next_points)
    print(f"{next_name} has {sum} points.")
    if sum >= max_point:
        max_point = sum
        winner = next_name
    if next_name == winner:
        print(f"{next_name} is the new number 1!")

print(f"{winner} won competition with {max_point} points!")
