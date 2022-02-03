'''
Usage
$ python dataset_upload.py --dataset_path "/dataset/local/directory/path/dataset.zip" --project_name toy_example --dataset_name dataset_name    
'''

from clearml import StorageManager, Dataset
import argparse
import os

def upload(args):
    manager = StorageManager()

    dataset_path = manager.get_local_copy(
        # remote_url="https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz"
        remote_url = args.dataset_path
    )

    dataset = Dataset.create(
        # dataset_name="Cleaml-dataset", dataset_project="minneapple_100_script"
        dataset_name=args.dataset_name, dataset_project=args.project_name
    )

    # Prepare and clean data here before it is added to the dataset
    dataset.add_files(path=dataset_path)
    # Dataset is uploaded to the ClearML Server by default
    dataset.upload()
    dataset.finalize()


def main():
    parser = argparse.ArgumentParser(description='Uploading dataset to clearML server')
    parser.add_argument('--dataset_path', type=str, help='enter dataset path or URL')
    parser.add_argument('--dataset_name', type=str, help='enter the dataset name')
    parser.add_argument('--project_name', type=str, help='enter the project name')
    args = parser.parse_args()

    upload(args)
    print("Finished")

if __name__ == '__main__':
    main()