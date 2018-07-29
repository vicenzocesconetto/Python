from pre_ml_library import parse_line, build_line_for_writing


DATASET_FILE_NAME = 'my-heart.csv'

ADAPTED_DATASET_NAME = 'new-my-heart.csv'

dataset = open(DATASET_FILE_NAME, 'r')

output_dataset = open(ADAPTED_DATASET_NAME, 'w')

for line in dataset:
    values = parse_line(line)
    if isinstance(values[0], str):
        output_dataset.write('age,sex,chest pain type 1,chest pain type 2,chest pain type 3,fasting blood sugar > 120 mg/dl,resting electrocardiographic results type 1,resting electrocardiographic results type 2,exercise induced angina,slope type 1,slope type 1,target\n')
        print('wrote a text line')

    else:
        values.insert(2, 0)
        values.insert(2, 0)

        values.insert(6, 0)

        values.insert(9, 0)

        if values[4] == 3:
            values[4] = 1
        elif values[4] == 2:
            values[4] = 0
            values[3] = 1
        elif values[4] == 1:
            values[4] = 0
            values[2] = 1
        elif values[4] != 0:
            print('this is unexpected')

        if values[7] == 2:
            values[7] = 1
        elif values[7] == 1:
            values[7] = 0
            values[6] = 1
        elif values[7] != 0:
            print('unpredicted')

        if values[10] == 2:
            values[10] = 1
        elif values[10] == 1:
            values[10] = 0
            values[9] = 1
        elif values[10] != 0:
            print('horsey')

        output_dataset.write(build_line_for_writing(values))

output_dataset.close()
dataset.close()