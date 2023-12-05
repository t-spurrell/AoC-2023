with open('day3/input.txt', 'r') as file:
    data = file.read().splitlines()

total = 0
for row_index, row in enumerate(data):
    for character_index, character in enumerate(row):
        if character != '*':
            continue

        points = set()

        for current_row in [row_index -1, row_index, row_index +1]:
            for current_column in [character_index-1, character_index, character_index+1]:
                if current_row < 0 or current_row >= len(data) or current_column < 0 or current_column >= len(data) or not data[current_row][current_column].isdigit():
                    continue
                while current_column > 0 and data[current_row][current_column -1].isdigit():
                    current_column -= 1
                points.add((current_row,current_column))

        if len(points) != 2:
            continue

        final = []

        for c_row, column in points:
            f = ''
            while column < len(data[c_row]) and data[c_row][column].isdigit():
                f += data[c_row][column]
                column += 1
            final.append(int(f))

        total += final[0] * final[1]
print(total)