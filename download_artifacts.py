
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

branch_zwave = "develop/23q2" 
branch_current_half_year = "develop/22q4"
rel_path = "../" #This scipt relative path to super or whatever repo you're using. Mine if Work/ArtifactDownloader, and Work/super, so I only need to .. 1 times
repo_name_that_you_are_using = rel_path + "super"

zwave_lib_destination_path = repo_name_that_you_are_using + "/protocol/z-wave/ZWave"
rail_lib_destination_path  = repo_name_that_you_are_using + "/platform/radio/rail_lib/autogen"
zpal_lib_destination_path  = repo_name_that_you_are_using + "/protocol/z-wave/platform/SiliconLabs/PAL"
zwave_bootloader_path      = repo_name_that_you_are_using + "/protocol/z-wave/UCBootLoader"

#-----------------------------------------------------------------------------------------------
# Parse the inputs first
parser = argparse.ArgumentParser(description="Download required libraries from jenkins for z-wave")
parser.add_argument('--zbranch',     type=str, help="branch of z-wave libs",      nargs='?', default = branch_zwave)
parser.add_argument('--branch',      type=str, help="branch of rail libs, nvm",   nargs='?', default = branch_current_half_year)
args = parser.parse_args()

def download_rail_libs(branch_name) -> None:
    print("Downloading RAIL libs...\n")
    global name_of_raillib_zip
    name_of_raillib_zip = "raillibs.zip"
    url_rail_libs = " http://iot-jenkins-master.silabs.com:8080/job/Gecko_SDK_Suite_RAIL_Continuous_Integration/job/" + branch_name +"/lastSuccessfulBuild/artifact/super/platform/radio/rail_lib/autogen/librail_release/*zip*/" + name_of_raillib_zip
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
    print("Download required libraries from jenkins for z-wave")
    delete_downloaded_files()

    branch_name = args.branch.replace("/", "%252F")  # Jenkins needs this
    zbranch_name = args.zbranch.replace("/", "%252F")  # Jenkins needs this

    download_zwave_libs(zbranch_name)
    download_zpal_libs(zbranch_name)
    download_bootloader_libs(branch_name)
    download_rail_libs(branch_name)
    extract_all_libs()
    handle_nvm_stuff()
    delete_downloaded_files()
    print("Done")

if __name__ == "__main__":
  main()
