# ClearML Tutorial-2  Dataset management
  This section covers how to upload data from the local system to clearML server using a script. The same can also be done using clearml-data from CLI.

  The dataset which we need to store should be zipped. And it can have videos, images, text files etc.

  Here we use StorageManager which is a helper interface for downloading & uploading files to supported remote storage Support remote servers: http(s)/S3/GS/Azure/File-System-Folder Cache is enabled by default for all downloaded remote urls/files. The given example downloads data from a URL and then pushes to the server. or it can also directly push a local copy of the dataset to the server. usage

  ```
  python dataset_upload.py --dataset_path "/dataset/local/directory/path/dataset.zip" --project_name toy_example --dataset_name dataset_name    
  ```

  Similarly we can use the below code to download the dataset.
  ```
  python dataset_download.py --dataset_path "/dataset/local/directory/path_to_save" --project_name toy_example --dataset_name dataset_name
  ```  
  
