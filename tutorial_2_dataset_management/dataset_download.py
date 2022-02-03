'''
Usage
$ python dataset_download.py --dataset_path "/dataset/local/directory/path_to_save" --project_name toy_example --dataset_name dataset_name    
'''

from clearml import StorageManager, Dataset
import argparse
import os

def download(args):
    manager = StorageManager()

    dataset = Dataset.get(
        dataset_name=args.dataset_name, 
        dataset_project=args.project_name).get_mutable_local_copy(args.dataset_path)


def main():
    parser = argparse.ArgumentParser(description='Uploading dataset to clearML server')
    parser.add_argument('--dataset_path', type=str, help='enter output dataset path')
    parser.add_argument('--dataset_name', type=str, help='enter the dataset name')
    parser.add_argument('--project_name', type=str, help='enter the project name')
    args = parser.parse_args()

    os.makedirs(args.dataset_path, exist_ok=True)

    download(args)
    print("Finished")

if __name__ == '__main__':
    main()