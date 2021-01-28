import os.path
import os
import csv


def save_data(results, file_name='results.csv', header= None, file_path=None):
    if header is None:
        header = 'Variety, artibute, mean, median, std \n'
    if file_path is None:
        file_path = os.getcwd()
    full_file_path = os.path.join(file_path, file_name)
    if os.path.exists(full_file_path):
        if input(f'File {file_name} in path {file_path} already exists. Do you want to overwrite? [Y/N] ') != 'Y':
            pass
        else:
            with open(full_file_path, mode='w') as csv_file:
                csv_file.write(header)
                for row in results:
                    csv_file.write(row)
                    csv_file.write('\n')
