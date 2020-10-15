from Dataset import Dataset
from Project import Project
from Label import Label_Object

def main():
    dataset = Dataset()
    project = Project()
    labelobj = Label_Object()

    #dataset.create_dataset("Hello", "Sample Description")
    dataset_dict = dataset.get_dataset(20)
    print(dataset_dict)
    

    #project.create_project("Birds", "Birds Project")
    project_dict = project.get_project(19)
    print(project_dict)

    #labelobj.create_Label("Rat", "BOUNDING_BOX")
    label_dict = labelobj.get_Label(33)
    print(label_dict)


if __name__ == '__main__':
    main()