from iris_analysis.io.load import load_data
from iris_analysis.io.save import save_data
from iris_analysis.calculate import calculate
from os.path import isfile
import argparse


def file_checker(filename):
    if not isfile(filename):
        raise argparse.ArgumentTypeError('File does not exists')
    return filename


def arguments_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=file_checker)
    parser.add_argument('output_file')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    save_data(calculate(load_data(arg.input_file, headers=True), target_column='variety'), file_name=arg.output_file,
              header=None, file_path=None)
