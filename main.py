from Dataset import Dataset
from Project import Project
from Label import Label_Object

def main():
    #dataset = Dataset()
    #project = Project()
    labelobj = Label_Object()

    #dataset.create_dataset("Hello", "Sample Description")
    #dataset.get_dataset(20)

    #project.create_project("Birds", "Birds Project")
    #project.get_project(19)

    #labelobj.create_Label("Rat", "BOUNDING_BOX")
    label_dict = labelobj.get_Label(33)
    print(label_dict)


if __name__ == '__main__':
    main()