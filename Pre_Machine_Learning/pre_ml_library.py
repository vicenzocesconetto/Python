

def parse_line(line: str) -> list:
    """Parses the line in the dataset, assuming it's a csv, and returns the values in a list"""
    parsed_line = line.replace('\n', '').split(',')

    try:
        parsed_line = [int(x) for x in parsed_line]
    except ValueError:
        return parsed_line

    return parsed_line


def build_line_for_writing(values: list) -> str:
    string = ""
    for value in values:
        string = string + str(value) + ','

    string = string[:-1]
    string += '\n'
    return string


def setup(learned_values_filename: str, number_of_seen_cases_filename: str, medical_conditions_weights: list) -> int:
    """Loads the values learned and the number of seen cases"""
    try:
        with open(learned_values_filename, 'r') as learned_values:
            for line in learned_values:
                medical_conditions_weights.append(parse_line(line))

    except IOError:
        open(learned_values_filename, "w").close()
        print(learned_values_filename + ' was created')

    number_of_seen_cases = 0

    try:
        with open(number_of_seen_cases_filename, 'r') as seen_cases_file:
            for line in seen_cases_file:
                number_of_seen_cases = parse_line(line)

    except IOError:
        open(number_of_seen_cases_filename, 'w').close()
        print(number_of_seen_cases_filename + ' was created')

    return number_of_seen_cases


def shutdown(learned_values_filename: str, learned_values: list, number_of_seen_cases_filename: str, seen_cases: int):
    with open(learned_values_filename, 'w') as learned_values_file:
        for value in learned_values:
            learned_values_file.write(value + '\n')
        learned_values_file.close()

    with open(number_of_seen_cases_filename, 'w') as seen_cases_file:
        seen_cases_file.write(str(seen_cases))
        seen_cases_file.close()
