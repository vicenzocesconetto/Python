import random


def check_for_snakes_and_ladders(snakes: list, ladders: list, current_position: int) -> int:
    for i in range(0, len(snakes), 2):
        if snakes[i] == current_position:
            return snakes[i+1]

    for i in range(0, len(ladders), 2):
        if ladders[i] == current_position:
            return ladders[i+1]

    return current_position


NUMBER_OF_PLAYERS = 2

INITIAL_SQUARE = 1

BOARD_SIZE = 36

DICE_SIDES = 6

AMOUNT_OF_SIMULATIONS = 10000

players_victories = [0] * NUMBER_OF_PLAYERS

ladders = [3, 16, 5, 7, 15, 25, 18, 20, 21, 32]

snakes = [12, 2, 14, 11, 17, 4, 31, 19, 35, 22]


for i in range(AMOUNT_OF_SIMULATIONS):
    players_positions = [INITIAL_SQUARE] * NUMBER_OF_PLAYERS
    # print('starting players_positions:' + str(players_positions))
    victory = False
    while not victory:
        for index in range(NUMBER_OF_PLAYERS):
            # print('player ' + str(index) + ' goes from ' + str(players_positions[index]), end='')
            players_positions[index] += random.randint(1, DICE_SIDES)
            # print(' to ' + str(players_positions[index]), end='')
            players_positions[index] = check_for_snakes_and_ladders(snakes, ladders, players_positions[index])
            # print(' and ends up in ' + str(players_positions[index]))
            if players_positions[index] >= BOARD_SIZE:
                victory = True
                players_victories[index] += 1
                break

    print('players positions end of game:' + str(players_positions))

print(players_victories)
