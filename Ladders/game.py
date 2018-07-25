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

INITIAL_SQUARE = 1  # Used in the initial versions

PLAYERS_INITIAL_POSITION = [1, 1]

# print(type(PLAYERS_INITIAL_POSITION))
print(PLAYERS_INITIAL_POSITION)

BOARD_SIZE = 36

DICE_SIDES = 6

AMOUNT_OF_SIMULATIONS = 10000

NUMBER_OF_META = 10

# Every even position is where the ladder starts and the following position is where is ends
ladders = [3, 16, 5, 7, 15, 25, 18, 20, 21, 32]

snakes = [12, 2, 14, 11, 17, 4, 31, 19, 35, 22]  # Same idea for the snakes list

am1 = [0] * NUMBER_OF_META
am2 = am1[:]

for iteration in range(NUMBER_OF_META):
    players_victories = [0] * NUMBER_OF_PLAYERS
    for i in range(AMOUNT_OF_SIMULATIONS):
        players_positions = PLAYERS_INITIAL_POSITION[:]
        # print(players_positions)
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

        # print('players positions end of game:' + str(players_positions))
    am1[iteration] = players_victories[0]
    am2[iteration] = players_victories[1]
    # print(players_victories)


print('player 1 arithmetic mean = ' + str(sum(am1)/len(am1)))
print('player 2 arithmetic mean = ' + str(sum(am2)/len(am2)))
