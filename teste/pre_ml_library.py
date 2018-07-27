

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
