
import argparse
from smartlabel.Dataset import Dataset
from smartlabel.Project import Project
from smartlabel.Label import Label_Object
from tabulate import tabulate

docstring = "*"*99 + """ Smartlabel command line interface.
""" +  "*"*99
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

parser.add_argument()
def main():
    args, leftovers = parser.parse_known_args()
    
    if hasattr(args, 'list_projects'):
        project = Project()
        table, columns= project.get_projects()
        output = tabulate(table, columns , tablefmt="psql")
        print(output)
    elif hasattr(args, 'create_project'):
        # TODO: list create a new project and return a line with its meta data.
        print('project has been created')
    elif hasattr(args, 'create_dataset'):
        # TODO: list create a new dataset and return a line with its meta data.
        print('dataset has been created')
    elif hasattr(args, 'create_dataset_row_from_csv'):
        # TODO: list create a new dataset and return a line with its meta data.
        print('all files have been uploaded to dataset')


        
    # else:
    #     if isinstance(int(args.list_projects),int):
    #         Id = int(args.list_projects)
    #         project = Project()
    #         table, columns= project.get_project(Id)
    #         output = tabulate(table, columns , tablefmt="psql")
    #         print(output)
    #     else:
    #         print("---------invalid Arguments, argument should be 'all' or by Project Id----------")
    
    # #else if ...:
    # #else if

if __name__ == '__main__':
    main()