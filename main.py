from Dataset import Dataset

def main():
    dataset = Dataset()

    dataset.create_dataset("Hello", "Sample Description")
    dataset.get_dataset(20)



if __name__ == '__main__':
    main()