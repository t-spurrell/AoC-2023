import re
with open("input.txt", "r") as file:
    data = file.readlines()

#data = ['28456eightwojbg', '25ksx49lrcroneightz','fnm3oneightsdn','two1nine','abcone2threexyz','4nineeightseven2','7pqrstsixteen']

def word_to_num(word: str) -> str:
    number_words = {"one":'1', "two":'2', "three":'3', "four":'4', "five":'5', "six":'6', "seven":'7', "eight":'8', "nine":'9'}
    return number_words.get(word)


def find_overlapping_matches(pattern, text) -> list:
    matches = []
    for i in range(len(text)):
        match = re.match(pattern, text[i:])
        if match:
            matches.append(match.group())
    return matches

def main():
    final = 0
    for line in data:
        nums = []
        #print(line)
        matches = find_overlapping_matches(r'(?:[0-9]|one|two|three|four|five|six|seven|eight|nine)', line.lower())
        #print(matches)
        nums.append(matches[0] if matches[0].isdigit() else word_to_num(matches[0]))
        nums.append(matches[-1] if matches[-1].isdigit() else word_to_num(matches[-1]))
        combined = ''.join(nums)
        final += int(combined)
    print(final)

main()