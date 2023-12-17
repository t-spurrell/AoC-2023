with open('day6/input.txt', 'r') as file:
    data = file.read().splitlines()

#print(data)
time = data[0].split()
time.pop(0)
#print(time)
distances = data[1].split()
distances.pop(0)
#print(distance)

total = 1
for time, distance in zip(time, distances):
    time = int(time)
    distance = int(distance)
    wins = 0
    for button_held in range(time):
        if button_held * (time-button_held) > distance:
            wins += 1
    
    total *= wins
print(total)
