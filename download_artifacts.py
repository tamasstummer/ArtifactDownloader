
print("""\
   _____      _         _          __  __    __                            _            _    _           
  / ____|    | |       | |        / _|/ _|  / _|                          | |          | |  (_)          
 | |  __  ___| |_   ___| |_ _   _| |_| |_  | |_ _ __ ___  _ __ ___        | | ___ _ __ | | ___ _ __  ___ 
 | | |_ |/ _ \ __| / __| __| | | |  _|  _| |  _| '__/ _ \| '_ ` _ \   _   | |/ _ \ '_ \| |/ / | '_ \/ __|
 | |__| |  __/ |_  \__ \ |_| |_| | | | |   | | | | | (_) | | | | | | | |__| |  __/ | | |   <| | | | \__ \ 
  \_____|\___|\__| |___/\__|\__,_|_| |_|   |_| |_|  \___/|_| |_| |_|  \____/ \___|_| |_|_|\_\_|_| |_|___/
                                                                                                         
""")

import os
import zipfile
import argparse
import json
import subprocess
import sys
import time
import shutil


branch_zwave = "develop/23q2" 
branch_current_half_year = "develop/23q2"
#-----------------------------------------------------------------------------------------------
# Parse the inputs first
parser = argparse.ArgumentParser(description="Download required libraries from jenkins for z-wave")
parser.add_argument('--zbranch',     type=str, help="branch of z-wave libs",      nargs='?',  default = branch_zwave)
parser.add_argument('--branch',      type=str, help="branch of rail libs, nvm",   nargs='?',  default = branch_current_half_year)
parser.add_argument('--debug',                 help="build z-wave and PAL debug libs",        action='count', default=0)
parser.add_argument('--only_debug',            help="only debug build, no download",          action='count', default=0)
parser.add_argument('--clean',                 help="remove s1 and s2 release, debug folders",action='count', default=0)
args = parser.parse_args()

def parse_config() -> json:
    try:
        print("Openning config.json...")
        with open("config.json") as config_file:
            config_file_string = config_file.read()
    except IOError:
        print("Can't open config.json file.")
        exit(1)

    try:
        config_file = json.loads(config_file_string)
        global repo_name_that_you_are_using
        if config_file["relPathEnable"] == True:
            repo_name_that_you_are_using = config_file["relPath"]
        else:
            repo_name_that_you_are_using = config_file["absPath"]
        
        global zwave_lib_destination_path
        global rail_lib_destination_path
        global zpal_lib_destination_path
        global zwave_bootloader_path
        
        zwave_lib_destination_path = repo_name_that_you_are_using + "/protocol/z-wave/ZWave"
        rail_lib_destination_path  = repo_name_that_you_are_using + "/platform/radio/rail_lib/autogen"
        zpal_lib_destination_path  = repo_name_that_you_are_using + "/protocol/z-wave/platform/SiliconLabs/PAL"
        zwave_bootloader_path      = repo_name_that_you_are_using + "/protocol/z-wave/UCBootLoader"
    except:
        print("Can't parse config.json file or invalid content")
        exit(1)
        
    return
            
def download_rail_libs(branch_name) -> None:
    print("Downloading RAIL libs...\n")
    global name_of_raillib_zip
    name_of_raillib_zip = "raillibs.zip"
    url_rail_libs = "https://zwave-jenkins.silabs.com/job/zw/job/zwave_platform_build/job/" + branch_name +"/lastSuccessfulBuild/artifact/platform/radio/rail_lib/autogen/librail_release/*zip*/" + name_of_raillib_zip
    os.system('wget ' + url_rail_libs)

def download_zwave_libs(branch_name) -> None:
    print("Downloading Z-Wave libs...\n")
    global name_of_zwave_lib_zip
    name_of_zwave_lib_zip = "libs.zip" 
    url_zwave_libs = "https://zwave-jenkins.silabs.com/job/zw-zwave/job/" + branch_name + "/lastSuccessfulBuild/artifact/ZWave/lib/*zip*/" + name_of_zwave_lib_zip
    os.system('wget ' + url_zwave_libs)

def download_zpal_libs(branch_name) -> None:
    print("Downloading Z-Wave ZPAL libs...\n")
    global name_of_zpal_lib_zip
    name_of_zpal_lib_zip = "zpallibs.zip"
    url_zpal_libs = "https://zwave-jenkins.silabs.com/job/zw-zwave/job/" + branch_name + "/lastSuccessfulBuild/artifact/platform/SiliconLabs/PAL/lib/*zip*/" + name_of_zpal_lib_zip
    os.system('wget ' + url_zpal_libs)

def download_bootloader_libs(branch_name) -> None:
    print("Downloading Bootloader files...\n")
    global name_of_bootloader_zip
    name_of_bootloader_zip = "bootloader.zip"
    url_bootloader_libs = "https://zwave-jenkins.silabs.com/job/zw/job/zwave_platform_build/job/" + branch_name + "/lastSuccessfulBuild/artifact/protocol/z-wave/UCBootLoader/build/*zip*/" + name_of_bootloader_zip
    os.system('wget ' + url_bootloader_libs)

def build_debug_libs() -> None:
    print("Building debug libraries...")
    try:
        os.chdir(f'{repo_name_that_you_are_using}/protocol/z-wave')
        python = "python3"
        if os.name == 'nt':
            python = "python.exe"
        
        cmd = f'{python} build.py --cmake --build --debug -VV'
        subprocess.run(cmd, stdout=sys.stdout, shell=True)
    except:
        exit(1)        

def remove_build_folder_s1_s2() -> None:
    print('Remove series1 and series2 directories from build')
    try:
        shutil.rmtree(f'{repo_name_that_you_are_using}/protocol/z-wave/build/series1')
    except FileNotFoundError:
        print('No series1 build found.')
    try:
        shutil.rmtree(f'{repo_name_that_you_are_using}/protocol/z-wave/build/series2')
    except FileNotFoundError:
        print('No series2 build found.')

def extract_all_libs() -> None:
    print("Extract zip files...\n")

    with zipfile.ZipFile(name_of_zwave_lib_zip, 'r') as zip_ref:
        zip_ref.extractall(zwave_lib_destination_path)

    with zipfile.ZipFile(name_of_zpal_lib_zip, 'r') as zip_ref:
        zip_ref.extractall(zpal_lib_destination_path)
    
    with zipfile.ZipFile(name_of_bootloader_zip, 'r') as zip_ref:
        zip_ref.extractall(zwave_bootloader_path)

    with zipfile.ZipFile(name_of_raillib_zip, 'r') as zip_ref:
        zip_ref.extractall(rail_lib_destination_path)

def delete_downloaded_files() -> None:
    print("Delete any ZIP files...\n")
    test = os.listdir('.')
    for item in test:
        if item.endswith(".zip"):
            os.remove(os.path.join('.', item))

def handle_nvm_stuff() -> None:
    print("Build nvm3_libs...\n")
    os.system("cd " + repo_name_that_you_are_using + "/platform/emdrv/nvm3 && make gcc")

def main() -> None:
    start_time = time.time()
    parse_config()
    print("Download required libraries from jenkins for z-wave")
    delete_downloaded_files()

    branch_name = args.branch.replace("/", "%252F")  # Jenkins needs this
    zbranch_name = args.zbranch.replace("/", "%252F")  # Jenkins needs this

    if args.only_debug != True:
        download_zwave_libs(zbranch_name)
        download_zpal_libs(zbranch_name)
        download_bootloader_libs(branch_name)
        download_rail_libs(branch_name)
        extract_all_libs()
        handle_nvm_stuff()
        delete_downloaded_files()
    if args.debug != 0 or args.only_debug:
        if args.clean != 0:
            remove_build_folder_s1_s2()
        build_debug_libs()
    print("Done")
    
    time_spent = time.time()-start_time
    print(f'Script run {time_spent} seconds and {time_spent / 60} minutes')

if __name__ == "__main__":
  main()
