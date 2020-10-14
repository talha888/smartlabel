from Dataset import Dataset
from Project import Project
from Label import Label_Object

def main():
    dataset = Dataset()
    project = Project()
    labelobj = Label_Object()

    #dataset.create_dataset("Hello", "Sample Description")
    dataset.get_dataset(20)

    #project.create_project("Birds", "Birds Project")
    project.get_project(19)

    #labelobj.create_Label("Rat", "BOUNDING_BOX")
    labelobj.get_Label(50)


if __name__ == '__main__':
    main()