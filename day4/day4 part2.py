with open('day4/input.txt', 'r') as file:
    data = file.read().splitlines()

data_length = len(data)
copies = [[] for _ in range(data_length+1)]
print(copies)
for i, d in enumerate(data):
    matches = 0
    card_id, all_numbers = d.split(":")
    winning_numbers, my_numbers = all_numbers.split('|')
    my_numbers = my_numbers.split()
    winning_numbers = winning_numbers.split()

    total = 0
    for my_number in my_numbers:
        if my_number in winning_numbers:
            total += 1

    for dup in range(i+1, i+total+1):
        copies[i].append(dup)

print('########################################')    
print(copies)
print('########################')

score = [0] + [1 for _ in range(data_length)]
print(score)
print('########################')

for i in range(data_length-1, -1, -1):
    for dup in copies[i]:
        score[i] += score[dup]

print(score)
print(sum(score))