import yaml
import os
import json


def read_yaml(path_to_yaml: str) -> dict: #it will be returning a dictionary of the config file if wegive the path of config.yaml file here
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)

    return content #it will returning as a dictionary


def create_directory(dirs: list): #we can pass a list.it will not return anything
    for dir_path in dirs:#iterate over that list
        os.makedirs(dir_path, exist_ok=True)
        print(f"directory is created at {dir_path}")


def save_local_df(data, data_path, index_status=False):
    data.to_csv(data_path, index=index_status)
    print(f"data is saved at {data_path}")


def save_reports(report: dict, report_path: str, indentation=4):
    with open(report_path, "w") as f:
        json.dump(report, f, indent=indentation)
    print(f"reports are saved at {report_path}")