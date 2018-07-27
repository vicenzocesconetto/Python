
def parse_line(line: str) -> list:
    """Parses the line in the dataset, assuming it's a csv, and returns the values in a list"""
    return line.split(',')


def build_line_for_writing(values: list) -> str:
    string = ""
    for value in values:
        string = string + str(values) + ','

    string[-1] = '\n'
    return string


DATASET_FILE_NAME = 'my-heart.csv'

ADAPTED_DATASET_NAME = 'new-my-heart.csv'

dataset = open(DATASET_FILE_NAME, 'r')

output_dataset = open(ADAPTED_DATASET_NAME, 'w')

for line in dataset:
    values = parse_line(line)
    if isinstance(values[0], str):
        output_dataset.write(line)
        print('wrote a text line')

    else:
        values.insert(3, 0)
        values.insert(3, 0)

        if values[5] == 3:
            values[5] = 1

        elif values[5] == 2:
            values[5] = 0
            values[4] = 1

        elif values[5] == 1:
            values[5] = 0
            values[3] = 1

        elif values[5] != 0:
                print('Oh ow, something went unpredictably bad')

        values.insert(7, 0)
        values.insert(7, 0)
        if values[]


