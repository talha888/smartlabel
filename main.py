from Dataset import Dataset
from Project import Project

def main():
    dataset = Dataset()
    project = Project()

    #dataset.create_dataset("Hello", "Sample Description")
    dataset.get_dataset(20)

    #project.create_project("Birds", "Birds Project")
    project.get_project(19)

if __name__ == '__main__':
    main()