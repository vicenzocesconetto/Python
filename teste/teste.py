
def setup(LEARNED_VALUES_FILENAME: str, NUMBER_OF_SEEN_CASES_FILENAME: str, medical_conditions_weights: list) -> int:
    """Loads the values learned and the number of seen cases"""
    try:
        with open(LEARNED_VALUES_FILENAME, 'r') as learned_values:
            for line in learned_values:
                medical_conditions_weights.append(int(line))

    except IOError:
        open(LEARNED_VALUES_FILENAME, "w").close()
        print(LEARNED_VALUES_FILENAME + ' was created')

    number_of_seen_cases = 0

    try:
        with open(NUMBER_OF_SEEN_CASES_FILENAME, 'r') as seen_cases_file:
            for line in seen_cases_file:
                number_of_seen_cases = int(line)

    except IOError:
        open(NUMBER_OF_SEEN_CASES_FILENAME, 'w').close()
        print(NUMBER_OF_SEEN_CASES_FILENAME + ' was created')

    return number_of_seen_cases


def parse_line(line: str) -> list:
    """Parses the line in the dataset, assuming it's a csv, and returns the values in a list"""
    return line.split(',')


def feed(dataset_filename: str, number_of_seen_cases: int):
    """This function is supposed to feed the data to the model"""
    with open(dataset_filename, 'r') as dataset:
        for line in dataset:
            dataset_line_values = parse_line(line)


def learn(case_values: list, number_of_seen_cases: int):
    if case_values[-1] == 0:
        return

    else:
        



def shutdown(learned_values_filename: str, learned_values: list, number_of_seen_cases_filename: str, seen_cases: int):
    with open(learned_values_filename, 'w') as learned_values_file:
        for value in learned_values:
            learned_values_file.write(value + '\n')
        learned_values_file.close()

    with open(number_of_seen_cases_filename, 'w') as seen_cases_file:
        seen_cases_file.write(str(seen_cases))
        seen_cases_file.close()


print('Power to the main thrusters')

LEARNED_VALUES_FILENAME = 'learned.txt'

NUMBER_OF_SEEN_CASES_FILENAME = 'seen_cases.txt'

CSV_LINE_LENGTH = 7

AMOUNT_OF_GOAL_VALUES = 1

dataset_filename = 'my-heart.csv'

medical_conditions_weights = list()

print('Initializing engines')

number_of_seen_cases = setup(LEARNED_VALUES_FILENAME, NUMBER_OF_SEEN_CASES_FILENAME, medical_conditions_weights)

if len(medical_conditions_weights) == 0:
    print('Seems like the files didnt exist')
    medical_conditions_weights = [0] * (CSV_LINE_LENGTH - AMOUNT_OF_GOAL_VALUES)

command = 1

while command:
    command = int(input('what do you want to do?\n'
                    '[0]Exit\n'
                    '[1]Train the model\n'))

    if command == 0:


    if command == 1:
        feed(dataset_filename, number_of_seen_cases)
