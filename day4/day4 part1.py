with open('day4/input.txt', 'r') as file:
    data = file.read().splitlines()

total = 0
for d in data:
    matches = 0
    card_id, all_numbers = d.split(":")
    winning_numbers, my_numbers = all_numbers.split('|')
    my_numbers = my_numbers.split()
    winning_numbers = winning_numbers.split()
    #print(type(my_numbers))
    for my_number in my_numbers:
        if my_number in winning_numbers:
            if matches > 0:
                matches *= 2
            else:
                matches += 1
    #print(matches)
    total += matches

print(total)
    # 1, 2, 3, 4, 5, 6
    # 1, 2, 4, 8, 16, 32