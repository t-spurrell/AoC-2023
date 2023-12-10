with open('day5/input.txt', 'r') as file:
    data = file.read().strip().split('\n\n')

seeds = data.pop(0)
seeds = seeds.split(':')[1].split()

new_seeds = []
for i in range(0, len(seeds), 2):
    sublist = [seeds[i], seeds[i + 1]]
    new_seeds.append(sublist)

locations = []
for new_seed in new_seeds:
    for seed in range(int(new_seed[0]), int(new_seed[0])+int(new_seed[1])):
        tracker = int(seed)
        for d in data:
            name, numbers_str = d.split(':')
            numbers_list = numbers_str.lstrip('\n').split('\n')
            #print(name)
            # print(numbers_list)
            for numbers in numbers_list:
                nums = numbers.split()
                #print(nums)
                if tracker in range(int(nums[1]), int(nums[1]) + int(nums[2])):
                    #print(f'in range. tracker is {tracker}. source start is {int(nums[1])} end is {int(nums[2])}')
                    diff = tracker - int(nums[1])
                    #print(f'diff is {diff}')
                    tracker = int(nums[0]) + diff
                    #print(f'new tracker value is {tracker}')
                    break
            

        locations.append(tracker)

locations.sort()
print(locations[0])