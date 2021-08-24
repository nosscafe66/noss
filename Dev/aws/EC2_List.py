import subprocess
import configparser
import pandas as pd
import json
from pandas.io.json import json_normalize

def read_param():
    Config = open('EC2_Config.ini', 'r')
    Config_list = Config.readlines()
    return Config_list

def join_param(Config_list):
    query = ','.join(Config_list)
    return query

def view_command(command_query):
    with open("EC2_List.json", "w") as outfile:
        query = "Reservations[].Instances[].{Name:Tags[?Key=='Name'].Value|[0]," + command_query + "}"
        command = subprocess.call(
            ['aws', 'ec2', 'describe-instances', '--query', query, '--output', 'table'], stdout=outfile)
        print(command)

def convert_to_csv():
    df = pd.read_json('EC2_List.json')
    df.to_csv("EC2_List.csv", encoding='utf-8')
        
if __name__ == "__main__":
    try:
        Config_list = read_param()
        #print(Config_list)
        command_query = join_param(Config_list)
        #print(command_query)
        view_command(command_query)
        print(view_command(command_query))
        #convert_to_csv()
    except Exception as errormessage:
        print("エラーです。："+str(errormessage))
