from src.utils.all_utils import read_yaml, create_directory
import argparse
import pandas as pd
import os

def get_data(config_path):
    config = read_yaml(config_path)#read_yaml to get the content of it
    # print(config) #to print all those present in config.yaml as a dictionary using the read yaml
    remote_data_path = config["data_source"] #call the data using the key-valu pair defined in the dictionary
    df = pd.read_csv(remote_data_path, sep=";")#we need to read it as a dataframe
    # print(df.head())# to print the data
#     # save dataset in the local directory or arifacts directory
#     # create path to directory: artifacts/raw_local_dir/data.csv
    artifacts_dir = config["artifacts"]['artifacts_dir']
    raw_local_dir = config["artifacts"]['raw_local_dir']
    raw_local_file = config["artifacts"]['raw_local_file']

    raw_local_dir_path = os.path.join(artifacts_dir, raw_local_dir)
    # print(raw_local_dir_path)
    create_directory(dirs= [raw_local_dir_path])#we need to ceate this in the artifacts folder
#   now we have the directory or path where we want to save our file
    raw_local_file_path = os.path.join(raw_local_dir_path, raw_local_file)
    # print(raw_local_file_path)
    df.to_csv(raw_local_file_path, sep=",", index=False)


#entry point for this load_save
if __name__ == '__main__': #defining this one first
    args = argparse.ArgumentParser() #initialise the object
    
    args.add_argument("--config", "-c", default="config/config.yaml")

    parsed_args = args.parse_args() #it takes command line argument
     
    # print(parsed_args) #by default it will be telling that this is config nd all
    # print(parsed_args.config)#gives default one which we passed it thru args.add_argument
    get_data(config_path=parsed_args.config)
