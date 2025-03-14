from configparser import ConfigParser
import random
import os
from pathlib import Path
config = ConfigParser()

def syscheck():
    files = os.listdir(".")
    if not Path('./config.ini').exists():
            print('Config file is not present\nCreating congig file...')
            Path('./config.ini').write_text('[main]')

    config.read('config.ini')
    if not config.has_section('main'):
        config.add_section('main')
        
    if not config.has_option('main','split_into'): 
        user_input=input('The files will be devided in to Mb: ')
        config.set('main', 'split_into', user_input)
        
    if not config.has_option('main','password'): 
        user_input=input('The password of your file: ')
        config.set('main', 'password', user_input)
        
    if not config.has_option('main','input_folder_name'): 
        user_input=input('The input folder name: ')
        config.set('main', 'input_folder_name', user_input)
        
    if not config.has_option('main','push_into_git'): 
        isSure = input('Are you sure, the backup will push into git? (y/n): ').lower().strip() == 'y'
        config.set('main', 'push_into_git', str(isSure))



    with open('config.ini', 'w') as f:
        config.write(f)
