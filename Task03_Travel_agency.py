city = input()
type_packet = input()
vip = input()
days = int(input())
exit = True

if days <= 0:
    print("Days must be positive number!")
    exit = False
elif city != "Bansko" and city != "Borovets" and city != "Varna" and city != "Burgas":
    print("Invalid input!")
    exit = False
elif city == "Bansko" or city == "Borovets":
    if type_packet == "withEquipment":
        sum = days * 100
        if vip == "yes":
            sum = sum * 0.9
    else:
        sum = days * 80
        if vip == "yes":
            sum = sum * 0.95
elif city == "Varna" or city == "Burgas":
    if type_packet == "withBreakfast":
        sum = days * 130
        if vip == "yes":
            sum = sum * 0.88
    else:
        sum = days * 100
        if vip == "yes":
            sum = sum * 0.97


if exit:
    print(f"The price is {sum:.2f}lv! Have a nice time!")



