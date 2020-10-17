from src.Dataset import Dataset
from src.Project import Project
from src.Label import Label_Object
import argparse
from tabulate import tabulate

parser = argparse.ArgumentParser(description='CLI interface for Smartlabel.digital')
parser.add_argument('--list-projects', nargs='?', help='List all user projects.')

# ? - none or more
# + - one or more
# 5

def main():
    args = parser.parse_args()
    

    if args.list_projects == 'all':
        project = Project()
        table, columns= project.get_projects()
        output = tabulate(table, columns , tablefmt="psql")
        print(output)
    else:
        if isinstance(int(args.list_projects),int):
            Id = int(args.list_projects)
            project = Project()
            table, columns= project.get_project(Id)
            output = tabulate(table, columns , tablefmt="psql")
            print(output)
        else:
            print("---------invalid Arguments, argument should be 'all' or by Project Id----------")
    
    #else if ...:
    #else if

if __name__ == '__main__':
    main()