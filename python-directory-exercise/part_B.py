import os
import csv


def sum_time_of_computation(set_model='A', main_path=None):
    if main_path is None:
        main_path = os.getcwd()

    time = 0 # result 

    for main_directory, _, files in os.walk(main_path, topdown=True): #we walk directories from top to bottom
        files = [file for file in files if file.endswith('.cvs')] # we choose desire file format
        for name in files:
            filename = f'{main_directory}/{name}'
            with open(filename, 'r') as file_content:
                reader = csv.reader(file_content, delimiter=';') # we choose file and separator
                next(reader) # we ommit the header
                for row in reader:
                    model, value, time_of_computation = [ch.replace(' ', 'k') for ch in row[:-1]]
                    print(f'{model}, {time_of_computation}')
                    if model == set_model:
                        time += int(time_of_computation[:-1]) #we ommit 's'
    return f'{time}s'
