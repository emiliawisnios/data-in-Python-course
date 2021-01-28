import csv


def load_data(csv_path, headers=True):
    dataset = []

    try:
        with open(csv_path, 'r') as data_file:
            reader = csv.reader(data_file)
            # set column names using first row
            if headers:
                columns = next(reader)

            # convert csv to dataset
            for row in reader:
                row_data = {}
                for i in range(len(row)):
                    # set key names
                    if headers:
                        row_key = columns[i].lower()
                    else:
                        row_key = i
                    # set key/value
                    row_data[row_key] = row[i]
                # add data to dataset
                dataset.append(row_data)

    # error handling
    except Exception as e:
        print(repr(e))

    return dataset
