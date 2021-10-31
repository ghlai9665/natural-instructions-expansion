import json
import os
from os import listdir, path
from os.path import isfile, join
from functools import partial

def get_all_files(tasks_path = '../tasks/'):
    files = []
    # find the task files containing the dataset
    for file_name in listdir(tasks_path):
        file = join(tasks_path, file_name)
        if isfile(file): files.append(file)
    files.sort()
    return files

def get_files_by_task_number(begin, end, tasks_path = '../tasks/'):
    files = get_all_files(tasks_path)
    return files[begin:end+1]


def get_files_by_ds(dataset_names = ["mctaco"], tasks_path = '../tasks/'):
    files = []
    # find the task files containing the dataset
    for file_name in listdir(tasks_path):
        file = join(tasks_path, file_name)
        if isfile(file) and any([dataset_name in file_name for dataset_name in dataset_names]):
            files.append(file)
    files.sort()
    return files

def modify_files(file, date_manipulate_func):
    """
    manipulate_data is a function that takes `data` as the sole argument and defines what you want to do to the file

    Usage: 

    >>> for file in files: 
    >>>    modify_files(file, date_manipulate_func)
    """
    with open(file, 'r') as f:
        data = json.load(f)
        date_manipulate_func(data)
        
    os.remove(file)
    with open(file, 'w') as f:
        modified_json = json.dumps(data, indent=4, ensure_ascii=False)
        print(modified_json, file=f)

def add_categories(category, data):
    data['Categories'].append(category)
    return data

def rename_categories(old_to_new_map, data):
    """
    Rename categories in task files
    
    Args:
        `old_to_new_map` should look like 
        {
            "old category name 1": "new category name 1",
            "old category name 2": "new category name 2"
        }
    """
    for i, category in enumerate(data["Categories"]):
        if category in old_to_new_map:
            data["Categories"][i] = old_to_new_map[category]
    return data

