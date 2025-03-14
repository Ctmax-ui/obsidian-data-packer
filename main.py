import os
from pathlib import Path
from utils.syscheck import syscheck
from configparser import ConfigParser
from utils.compresser import zip_with_7z
from utils.upload_into_git import gitCommiter

config = ConfigParser()
syscheck()

output_folder_path='output'
for file in os.listdir(output_folder_path):
    file_path = os.path.join(output_folder_path, file)
    if os.path.isfile(file_path):
        os.remove(file_path)
        
config.read('config.ini')
password= config.get('main','password')
split_into= config.get('main','split_into')
input_folder=config.get('main','input_folder_name')
push_into_git=config.get('main','push_into_git')

zip_with_7z(input_folder, output_folder_path+"/secure_archive",password, split_into or 20)

if push_into_git == 'True':
    gitCommiter(output_folder_path)