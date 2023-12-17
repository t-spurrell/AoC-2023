with open('day5/input.txt', 'r') as file:
    inputs, *data = file.read().strip().split('\n\n')

inputs = list(map(int, inputs.split(":")[1].split()))
# inputs = data.pop(0)
# inputs = inputs.split(':')[1].split()

seeds = []
for i in range(0, len(inputs), 2):
    seeds.append((inputs[i], inputs[i] + inputs[i + 1]))


for d in data:
    ranges = []
    for line in d.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    # name, numbers_str = d.split(':')
    # ranges = numbers_str.lstrip('\n').split('\n')
    # ranges = [x.split() for x in ranges]
    print(ranges)
    #print(name)
    # print(numbers_list)
    new = []
    while len(seeds) > 0:
        s, e = seeds.pop()
        for a, b, c in ranges:
            os = max(s, b)
            oe = min(e, b + c)
            if os < oe:
                new.append((os - b + a, oe - b + a))
                if os > s:
                    seeds.append((s, os))
                if e > oe:
                    seeds.append((oe, e))
                break
        else:
            new.append((s, e))
    seeds = new

print(min(seeds)[0])
#     for numbers in numbers_list:
#         nums = numbers.split()
#         #print(nums)
#         if tracker in range(int(nums[1]), int(nums[1]) + int(nums[2])):
#             #print(f'in range. tracker is {tracker}. source start is {int(nums[1])} end is {int(nums[2])}')
#             diff = tracker - int(nums[1])
#             #print(f'diff is {diff}')
#             tracker = int(nums[0]) + diff
#             #print(f'new tracker value is {tracker}')
#             break
        

#     locations.append(tracker)

# locations.sort()
# print(locations[0])