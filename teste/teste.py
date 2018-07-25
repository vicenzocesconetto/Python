
def setup(LEARNED_VALUES_FILENAME: str, NUMBER_OF_SEEN_CASES_FILENAME: str, medical_conditions_weights: list) -> int:
    """Loads the values learned and the number of seen cases"""
    try:
        with open(LEARNED_VALUES_FILENAME, 'r') as LEARNED_VALUES_FILE:
            for line in LEARNED_VALUES_FILE:
                medical_conditions_weights.append(int(line))

    except IOError:
        open(LEARNED_VALUES_FILENAME, "w").close()
        print(LEARNED_VALUES_FILENAME + ' was created')


    number_of_seen_cases = 0

    try:
        with open(NUMBER_OF_SEEN_CASES_FILENAME, 'r') as NUMBER_OF_SEEN_CASES_FILE:
            for line in NUMBER_OF_SEEN_CASES_FILE:
                number_of_seen_cases = int(line)

    except IOError:
        open(NUMBER_OF_SEEN_CASES_FILENAME, 'w').close()
        print(NUMBER_OF_SEEN_CASES_FILENAME + ' was created')

    return number_of_seen_cases


def parse_line(line: str) -> list:
    """Parses the line in the dataset, assuming it's a csv, and returns the values in a list"""
    return line.split(',')


def feed(DATASET_FILENAME: str):
    """This function is supposed to feed the data to the model"""
    with open(DATASET_FILENAME, 'r') as dataset:
        for line in dataset:
            dataset_line_values = parse_line(line)


def __main__():
    print('Power to the main thrusters')

    LEARNED_VALUES_FILENAME = 'learned.txt'

    NUMBER_OF_SEEN_CASES_FILENAME = 'seen_cases.txt'

    medical_conditions_weights = list()

    print('Initializing engines')

    number_of_seen_cases = setup(LEARNED_VALUES_FILENAME, NUMBER_OF_SEEN_CASES_FILENAME, medical_conditions_weights)

    if len(medical_conditions_weights) == 0:
        size = input('seems like the files dint exist, did they? Well, what is the amount of conditions?\n')
        for i in range(0, int(size)):
            medical_conditions_weights.append(0)

    command = 1

    while command:
        command = int(input('what do you want to do?\n'
                        '[0]Exit\n'
                        '[1]Train the model\n'))
