
import argparse
from smartlabel.Dataset import Dataset
from smartlabel.Project import Project
from smartlabel.Label import Label_Object
from tabulate import tabulate

docstring = "*"*99 + """ Smartlabel command line interface.
""" +  "*"*99
parser = argparse.ArgumentParser(description=docstring)
parser.add_argument("--list-projects", default=argparse.SUPPRESS, nargs='?')
parser.add_argument("--get-project", default=argparse.SUPPRESS, nargs='?')
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
        if args.list_projects is None:
            project = Project()
            table, columns= project.get_projects()
            if table != 0:
                output = tabulate(table, columns , tablefmt="psql")
                print(output)
            else:
                print("-----------------NO RECORD FOUND-----------------")
        else:
            print("-----------------To do , Need to show help-----------------")

    elif hasattr(args, 'get_project'):
        Id = args.get_project
        project = Project()
        table, columns= project.get_project(Id)
        if table != 0:
            output = tabulate(table, columns , tablefmt="psql")
            print(output)
        else:
            print("-----------------TRY WITH VALID ID-----------------")
    
    elif hasattr(args, 'create_project'):
        if args.create_project is not None:
            Createdby,DatasetId, Name, Description, Status, Role = input("Enter the following data Createdby,DatasetId, Name, Description, Status, Role: ").split() 
            project = Project()
            project.create_project(Createdby,DatasetId, Name, Description, Status, Role)
        else:
            print("-----------------Invalid entry-----------------")
            
    elif hasattr(args, 'create_dataset'):
        # TODO: list create a new dataset and return a line with its meta data.
        print(args)
    elif hasattr(args, 'create_dataset_row_from_csv'):
        # TODO: list create a new dataset and return a line with its meta data.
        print('all files have been uploaded to dataset')


if __name__ == '__main__':
    main()