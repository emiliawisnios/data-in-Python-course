import statistics


def calculate(dataset, target_column='variety'):
    results = []

    # finding values of target column
    target_column_values = []
    for row in dataset:
        target_column_values.append(row[target_column])
    unique_target_column_values = list(set(target_column_values))

    numeric_column_names = []
    string_column_names = []
    first_row = dataset[0]

    # finding all numeric columns
    for column_name in first_row.keys():
        try:
            float(first_row[column_name])
            numeric_column_names.append(column_name)
        except ValueError:
            string_column_names.append(column_name)


    for value in unique_target_column_values:
        for column_name in numeric_column_names:
            column_numeric_values = [float(row[column_name]) for row in dataset if row[target_column] == value]
            results.append((f'{value},{column_name},{statistics.mean(column_numeric_values)},'
                            f'{statistics.median(column_numeric_values)},{statistics.stdev(column_numeric_values)}'))
    return results
