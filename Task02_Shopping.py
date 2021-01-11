budget = float(input())
video_cards = int(input())
cpu = int(input())
ram = int(input())

#sum = (video_cards * 250) + ((video_cards * 250) * 0.35 * cpu) + (((video_cards * 250) * 0.35) * 0.1 * cpu * ram)
video_cards_price = video_cards * 250
cpu_price = video_cards_price * 0.35 * cpu
ram_price = video_cards_price * 0.1 * ram

sum = video_cards_price + cpu_price + ram_price

if video_cards > cpu:
    sum = sum * 0.85

if budget >= sum:
    print(f"You have {budget - sum:.2f} leva left!")
else:
    print(f"Not enough money! You need {sum - budget:.2f} leva more!")