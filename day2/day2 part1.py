def get_game_info_dict() -> dict:
    with open("input.txt", "r") as file:
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
game_ids = []
for game_id, game_rounds in games.items():
    game_id = int(game_id)
    game_ids.append(game_id)
    for game_round in game_rounds:
        green = game_round.get('green')
        red = game_round.get('red')
        blue = game_round.get('blue')
        green = int(green) if green else 0
        red = int(red) if red else 0
        blue = int(blue) if blue else 0

        if red > 12 or green > 13 or blue > 14:
            #print(f'game_id: {game_id} red:{red}, blue:{blue}, green:{green}')
            game_ids.remove(game_id)
            break

print(sum(game_ids))