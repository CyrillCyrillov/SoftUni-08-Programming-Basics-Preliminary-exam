numbers = int(input())
back = 0
chest = 0
legs = 0
abss = 0
protein_shake = 0
protein_bar = 0

for i in range(1, numbers+1):
    type_client = input()
    # (, "Chest", , ",  или
    if type_client == "Back":
        back += 1
    elif type_client == "Chest":
        chest += 1
    elif type_client == "Legs":
        legs += 1
    elif type_client == "Abs":
        abss += 1
    elif type_client == "Protein shake":
        protein_shake += 1
    elif type_client == "Protein bar":
        protein_bar += 1

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abss} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{(back + chest + legs + abss) / numbers * 100:.2f}% - work out")
print(f"{(protein_bar + protein_shake) / numbers *100:.2f}% - protein")


