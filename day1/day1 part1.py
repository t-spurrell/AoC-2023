with open("input.txt", "r") as file:
    data = file.readlines()

final = 0

for line in data:
    nums = []
    for char in line:
        if char.isdigit():
            nums.append(char)
            break
    for char in line[::-1]:
        if char.isdigit():
            nums.append(char)
            break
    if nums:
        number = ''.join(nums)
        print(number)
        final += int(number)

print(final)

