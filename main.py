
import argparse
from smartlabel.Dataset import Dataset
from smartlabel.Project import Project
from smartlabel.Label import Label_Object
from tabulate import tabulate
import sys
import requests
import json
from pathlib import Path
from os.path import join
import os
from shutil import rmtree

API_URL = 'http://127.0.0.1:5000/'
home = str(Path.home())
CONFIG_FILE_FOLDER = join(home, '.smartlabel')
CONFIG_FILE_PATH = join(CONFIG_FILE_FOLDER, 'config')


docstring = "*"*99 + """ Smartlabel command line interface.
""" +  "*"*99
parser = argparse.ArgumentParser(description=docstring)

parser.add_argument("--login", default=argparse.SUPPRESS, nargs=2, help="Enter two arguments, api key and api seceret.")
parser.add_argument("--logout", default=argparse.SUPPRESS, nargs="?")

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

def get_token():
    if not os.path.exists(CONFIG_FILE_PATH):
        return False
    try:
        with open(CONFIG_FILE_PATH, 'r') as f:
            token = json.load(f)
        return token['token']
    except Exception as e:
        return False

def main():
    args, leftovers = parser.parse_known_args()
    
    if hasattr(args, 'logout'):
        result = input("Are you sure? [Y/N]")
        result = result.lower()
        if  result == 'y' or result == 'yes':
            rmtree(CONFIG_FILE_FOLDER)
        else:
            print('Could not logout.')
        sys.exit(0)


    token = get_token()
    if not token:
        if hasattr(args, 'login'):
            try:
                key, seceret = args.login
                result = requests.post(f"{API_URL}/get_token", json={"API_KEY": key, "API_SECERET": seceret})
                token = json.loads(result.text)
                data = {"API_KEY": key, "API_SECERET": seceret, 'token': token['token']}
                if not os.path.exists(CONFIG_FILE_PATH):
                    os.mkdir(join(home, '.smartlabel'))
                with open(CONFIG_FILE_PATH, 'w') as f:
                    json.dump(data, f)
                print('Welcome --- ')
                sys.exit(0)        
            except Exception as e:
                print('ERROR', e)
        
        print('Use --login to create a token so you can communicate with serer.')
        sys.exit(0)
    
    headers = {'x-access-token': token}
    if hasattr(args, 'list_projects'):
        if args.list_projects is None:
            try:
                res = requests.get(f"{API_URL}/list_projects", headers=headers)
                project_list = json.loads(res.text)
                print(project_list)
            except Exception as e:
                pass
            # project = Project()
            # table, columns= project.get_projects()
            # if table != 0:
            #     output = tabulate(table, columns , tablefmt="psql")
            #     print(output)
            # else:
            #     print("-----------------NO RECORD FOUND-----------------")
        else:
            parser.print_help

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