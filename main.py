docstring = "*"*99 + """ Smartlabel command line interface.
""" +  "*"*99

import argparse


parser = argparse.ArgumentParser(description=docstring)

parser.add_argument("--list-projects", default=argparse.SUPPRESS, nargs='?')

parser.add_argument("--create-project", default=argparse.SUPPRESS, nargs=1)
parser.add_argument("--create-dataset", default=argparse.SUPPRESS, nargs=1)
parser.add_argument("--create-dataset-rows-from-directory", default=argparse.SUPPRESS, nargs=1)
parser.add_argument("--create-dataset-row-from-s3", default=argparse.SUPPRESS, nargs=1, type=str)
parser.add_argument("--create-dataset-row-from-csv", default=argparse.SUPPRESS, nargs=1, type=str)
parser.add_argument("--create-dataset-row-from-txt", default=argparse.SUPPRESS, nargs=1, type=str)
parser.add_argument("--create-dataset-row-from-image", default=argparse.SUPPRESS, nargs=1, type=str)


parser.add_argument("--connect-dataset-to-project", default=argparse.SUPPRESS, nargs=1)


# TODO: add argparse support to the module
# TODO: https://github.com/talha888/smartlabel/issues/1


def main():
    args, leftovers = parser.parse_known_args()
    
    if hasattr(args, 'list_projects'):
        # TODO: list all projects with tabulate
        print('list projects')
    elif hasattr(args, 'create_project'):
        # TODO: list create a new project and return a line with its meta data.
        print('project has been created')
    elif hasattr(args, 'create_dataset'):
        # TODO: list create a new dataset and return a line with its meta data.
        print('dataset has been created')
    elif hasattr(args, 'create_dataset_row_from_csv'):
        # TODO: list create a new dataset and return a line with its meta data.
        print('all files have been uploaded to dataset')



if __name__ == '__main__':
    main()