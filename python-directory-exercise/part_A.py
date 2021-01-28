  
import random
import os
import itertools
import os.path

# function that generates text for files consistent with task description
def file_content_generator(options=['A','B','C'], min_random_value_1=0, max_random_value_1=1000,
                           min_random_value_2=0, max_random_value_2=1000):

    header = 'Model; Output value; Time of computation; \n'
    model = random.choice(options) # function random.choice chooses randomly one of the options from the given set
    value = random.randint(min_random_value_1, max_random_value_1) # function random.randint chooses randomly numbers from given range
    time_of_computation = random.randint(min_random_value_2, max_random_value_2)

    return f'{header}{model} ; {value} ; {time_of_computation}s; \n'


# function that creates directories and files
def directories_and_files_maker(main_path=None, directories=None, file_name=None):
    if main_path is None:
        main_path=os.getcwd()
    if directories is None:
        directories = list(itertools.product(['Monday', 'Tuesday', 'Wednesday', 'Friday', 'Saturday', 'Sunday'],
                                             ['morning', 'evening']))
    if file_name is None:
        file_name = 'Solutions.cvs'
    # all conditional statements above allow us quickly to change parameters of the given task

    for folders in itertools.product(directories): # we create cartesian product of given set of directories
        filepath = '/'.join(*folders)
        new_path = f'{main_path}/{filepath}'
        if os.path.exists(new_path):
            if input(f'Directory {new_path} already exists. Do you want to overwrite? [Y/N] ') != 'Y':
                continue
            else:
                os.makedirs(new_path, exist_ok=True) # exist_ok overwrites directory
        final_path = f'{main_path}/{filepath}/{file_name}'
        if os.path.exists(final_path):
            if input(f'File {file_name} in path {final_path} already exists. Do you want to overwrite? [Y/N] ') != 'Y':
                continue
            else:
                with open(final_path, 'w') as file:
                    file.write(file_content_generator())

directories_and_files_maker()
