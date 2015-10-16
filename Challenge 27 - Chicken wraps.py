#Challenge 27
print("\t\tTortilla\t\tChicken\t\tSalad\t\tChilli Sauce")
count = 1
for tortilla in (0,1):
    for chicken in (0,1):
        for salad in (0,1):
            for chillisauce in (0,1):
                cost = 0
                if tortilla:
                    cost += 0.25
                if chicken:
                    cost += 0.55
                if salad:
                    cost += 0.12
                if chillisauce:
                    cost += 0.24
                print("#", count, end='')
                print("  \t\t",chillisauce, "  \t\t", salad, "  \t\t", chicken, "  \t\t", tortilla, "  \t\t", cost)
                count += 1
