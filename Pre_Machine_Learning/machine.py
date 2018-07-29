from pre_ml_library import parse_line, setup, shutdown


def feed(dataset_filename: str, number_of_seen_cases: int):
    """This function is supposed to feed the data to the model"""



def learn(case_values: list, variable_weights: list, number_of_seen_cases: int) -> int:
    if len(case_values) - 1 != len(variable_weights):
        print('case mismatch')

    elif case_values[-1] != 0:
        print('learning')
        for i in range(len(case_values)-1):
            variable_weights[i] = (case_values[i] + (variable_weights[i] * number_of_seen_cases)) / number_of_seen_cases + 1

        number_of_seen_cases += 1

    return number_of_seen_cases


print('Power to the main thrusters')

LEARNED_VALUES_FILENAME = 'learned_values'

NUMBER_OF_SEEN_CASES_FILENAME = 'number_of_seen_cases'

CSV_LINE_LENGTH = 12

AMOUNT_OF_GOAL_VALUES = 1

dataset_filename = 'new-my-heart.csv'

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
        shutdown(LEARNED_VALUES_FILENAME, medical_conditions_weights, NUMBER_OF_SEEN_CASES_FILENAME, number_of_seen_cases)

    elif command == 1:
        with open(dataset_filename, 'r') as dataset:
            dataset.readline()
            for line in dataset:
                dataset_line_values = parse_line(line)
