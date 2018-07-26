
def parse_line(line: str) -> list:
    """Parses the line in the dataset, assuming it's a csv, and returns the values in a list"""
    return line.split(',')


DATASET_FILE_NAME = 'my-heart.csv'

ADAPTED_DATASET_NAME = 'new-my-heart.csv'

dataset = open(DATASET_FILE_NAME, 'r')

output_dataset = open(ADAPTED_DATASET_NAME, 'w')

for line in dataset:
    values = parse_line(line)
    if()
