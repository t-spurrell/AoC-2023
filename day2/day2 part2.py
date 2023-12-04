def get_game_info_dict() -> dict:
    with open("day2/input.txt", "r") as file:
        games = file.readlines()

    end_result = {}
    for game in games:
        game_id , results = game.split(':')
        game_id = game_id.strip('Game ')
        end_result[game_id] = []
        results = results.strip('\n').split(';')
        #print(results)
        for result in results:
            result = result.strip().split(',')
            x = {combo.split()[1]:combo.split()[0] for combo in result}
            end_result[game_id].append(x)
    return end_result


games = get_game_info_dict()
powers = []
for game_id, game_rounds in games.items():
    min_red = 0
    min_blue = 0
    min_green = 0
    for game_round in game_rounds:
        green = game_round.get('green')
        red = game_round.get('red')
        blue = game_round.get('blue')
        green = int(green) if green else 0
        red = int(red) if red else 0
        blue = int(blue) if blue else 0

        if red > min_red:
            min_red = red
        if blue > min_blue:
            min_blue = blue
        if green > min_green:
            min_green = green
            
    power = (min_red*min_blue*min_green)
    powers.append(power)
 
print(sum(powers))