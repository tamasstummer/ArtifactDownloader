import os
import wget
import shutil
import time
import argparse

local_gsdk_path = "C:/SiliconLabs/super/"

def download_rail_artifacts(build_number, branch_name):

    relative_path_to_gsdk = f"platform/radio/rail_lib/autogen"
    rail_libs = [
    # "/librail_release/librail_config_zgm130s037hgn1_gcc.a",
    "/librail_release/librail_config_zgm130s037hgn_gcc.a",
    # "/librail_release/librail_config_zgm230sa27hgn_gcc.a",
    "/librail_release/librail_config_zgm230sa27hnn_gcc.a",
    "/librail_release/librail_config_zgm230sb27hgn_gcc.a",
    # "/librail_release/librail_module_efr32xg12_gcc_release.a",
    "/librail_release/librail_module_efr32xg13_gcc_release.a",
    # "/librail_release/librail_module_efr32xg14_gcc_release.a",
    # "/librail_release/librail_module_efr32xg1_gcc_release.a",
    # "/librail_release/librail_module_efr32xg21_gcc_release.a",
    # "/librail_release/librail_module_efr32xg22_gcc_release.a",
    "/librail_release/librail_module_efr32xg23_gcc_release.a",
    # "/librail_release/librail_module_efr32xg24_gcc_release.a",
    # "/librail_release/librail_module_efr32xg25_gcc_release.a",
    # "/librail_release/librail_module_efr32xg26_gcc_release.a",
    # "/librail_release/librail_module_efr32xg27_gcc_release.a",
    # "/librail_release/librail_module_efr32xg28_gcc_release.a",
    # "/librail_release/librail_efr32xg12_gcc_release.a",
    "/librail_release/librail_efr32xg13_gcc_release.a",
    "/librail_release/librail_efr32xg14_gcc_release.a",
    # "/librail_release/librail_efr32xg1_gcc_release.a",
    # "/librail_release/librail_efr32xg21_gcc_release.a",
    # "/librail_release/librail_efr32xg22_gcc_release.a",
    "/librail_release/librail_efr32xg23_gcc_release.a",
    # "/librail_release/librail_efr32xg24_gcc_release.a",
    # "/librail_release/librail_efr32xg25_gcc_release.a",
    # "/librail_release/librail_efr32xg26_gcc_release.a",
    # "/librail_release/librail_efr32xg27_gcc_release.a",
    "/librail_release/librail_efr32xg28_gcc_release.a",
    "/ver.h",
    "/ver_def.h"
    ]
    for lib in rail_libs:
        download_libs(build_number, branch_name, relative_path_to_gsdk, lib)
    print("   rail libs downloaded")

def download_nvm3_artifacts(build_number, branch_name):
    relative_path_to_gsdk = f"platform/emdrv/nvm3/lib"
    nvm3_libs = [
    "/libnvm3_CM0P_gcc.a",
    "/libnvm3_CM33_gcc.a",
    "/libnvm3_CM3_gcc.a",
    "/libnvm3_CM4_gcc.a"
    ]

    for lib in nvm3_libs:
        download_libs(build_number, branch_name, relative_path_to_gsdk, lib)
    print("   nvm3 libs downloaded")

def download_ZW_libs(build_number, branch_name):
    relative_path_to_gsdk = f"protocol/z-wave/ZWave/lib"
    zw_libs = [
        "/libZWaveController_700s.a",
        "/libZWaveController_800s.a",
        "/libZWaveSlave_700s.a",
        "/libZWaveSlave_800s.a"
    ]
    for lib in zw_libs:
        download_libs(build_number, branch_name, relative_path_to_gsdk, lib)
    print("   ZW libs downloaded")

def download_ZPAL_libs(build_number, branch_name):

    relative_path_to_gsdk = f"protocol/z-wave/platform/SiliconLabs/PAL/lib"
    zpal_libs = [
    # "/libzpal_efr32zg14p231f256gm32.a",
    # "/libzpal_efr32zg14p731f256gm32.a",
    # "/libzpal_efr32zg23a010f512gm40.a",
    # "/libzpal_efr32zg23a010f512gm48.a",
    # "/libzpal_efr32zg23a020f512gm40.a",
    # "/libzpal_efr32zg23a020f512gm48.a",
    # "/libzpal_efr32zg23b010f512im40.a",
    # "/libzpal_efr32zg23b010f512im48.a",
    # "/libzpal_efr32zg23b011f512im40.a",
    # "/libzpal_efr32zg23b020f512im40.a",
    # "/libzpal_efr32zg23b020f512im48.a",
    # "/libzpal_efr32zg23b021f512im40.a",
    # "/libzpal_efr32zg28a110f1024gm48.a",
    # "/libzpal_efr32zg28a110f1024gm68.a",
    # "/libzpal_efr32zg28a112f1024gm48.a",
    # "/libzpal_efr32zg28a112f1024gm68.a",
    # "/libzpal_efr32zg28a120f1024gm48.a",
    # "/libzpal_efr32zg28a120f1024gm68.a",
    # "/libzpal_efr32zg28a122f1024gm48.a",
    # "/libzpal_efr32zg28a122f1024gm68.a",
    # "/libzpal_efr32zg28b310f1024im48.a",
    # "/libzpal_efr32zg28b310f1024im68.a",
    # "/libzpal_efr32zg28b312f1024im48.a",
    # "/libzpal_efr32zg28b312f1024im68.a",
    # "/libzpal_efr32zg28b320f1024im48.a",
    # "/libzpal_efr32zg28b320f1024im68.a",
    # "/libzpal_efr32zg28b322f1024im48.a",
    # "/libzpal_efr32zg28b322f1024im68.a",
    "/libzpal_zgm130s037hgn.a",
    "/libzpal_zgm130s037hgn1.a",
    "/libzpal_zgm230sa27hgn.a",
    "/libzpal_zgm230sa27hnn.a",
    "/libzpal_zgm230sb27hgn.a",
    "/libzpal_zgm230sb27hnn.a"
    ]

    for lib in zpal_libs:
        download_libs(build_number, branch_name, relative_path_to_gsdk, lib)
    print("   ZPAL libs downloaded")

def download_bootloaders(build_number, branch_name):
    relative_path_to_gsdk = f"protocol/z-wave/Apps/bin"
    bootloader_libs = [
        "/ota-EFR32FG28_BRD4400A-crc.s37",
        "/ota-EFR32FG28_BRD4401A-crc.s37",
        # "/ota-EFR32ZG23_BRD4204A-crc.s37",
        # "/ota-EFR32ZG23_BRD4204B-crc.s37",
        # "/ota-EFR32ZG23_BRD4204C-crc.s37",
        "/ota-EFR32ZG23_BRD4204D-crc.s37",
        "/ota-EFR32ZG23_BRD4210A-crc.s37",
        "/ota-EFR32ZG28_BRD2705A-crc.s37",
        "/ota-EFR32ZG28_BRD4400B-crc.s37",
        "/ota-EFR32ZG28_BRD4400C-crc.s37",
        "/ota-EFR32ZG28_BRD4401B-crc.s37",
        "/ota-EFR32ZG28_BRD4401C-crc.s37",
        "/ota-ZGM230S_BRD2603A-crc.s37",
        # "/ota-ZGM230S_BRD4205A-crc.s37",
        "/ota-ZGM130S_BRD4207A-combined.s37",
        "/ota-ZGM230S_BRD4205B-crc.s37"
    ]

    for lib in bootloader_libs:
        download_bootloader_libs(build_number, branch_name, relative_path_to_gsdk, lib)
    print("   bootloader libs downloaded")

def download_libs(build_number, branch_name, relative_path_to_gsdk, lib):
    url = f"https://artifactory.silabs.net/artifactory/gsdk-generic-development/{branch_name}/{build_number}/gecko-sdk.zip!/{relative_path_to_gsdk}{lib}"
    # print(url)
    filename = wget.download(url, out=local_gsdk_path + relative_path_to_gsdk + lib)
    # print("\n" + filename.split('/')[-1] + " downloaded")

def download_bootloader_libs(build_number, branch_name, relative_path_to_gsdk, lib):
    url = f"https://artifactory.silabs.net/artifactory/gsdk-generic-development/{branch_name}/{build_number}/demo-applications.zip!/{relative_path_to_gsdk}{lib}"
    # print(url)
    filename = wget.download(url, out=local_gsdk_path + relative_path_to_gsdk + lib)
    # print("\n" + filename.split('/')[-1] + " downloaded")

def handle_environment_before_download():
    #check if librail_release folder exists, if not create it, if yes delete it and create it again
    if os.path.exists(local_gsdk_path + "platform/radio/rail_lib/autogen/librail_release"):
        shutil.rmtree(local_gsdk_path + "platform/radio/rail_lib/autogen/librail_release")
    os.makedirs(local_gsdk_path + "platform/radio/rail_lib/autogen/librail_release")
    print("librail_release folder created")

    #check if libnvm3 folder exists, if not create it, if yes delete it and create it again
    if os.path.exists(local_gsdk_path + "platform/emdrv/nvm3/lib"):
        shutil.rmtree(local_gsdk_path + "platform/emdrv/nvm3/lib")
    os.makedirs(local_gsdk_path + "platform/emdrv/nvm3/lib")
    print("libnvm3 folder created")

    #check if libzwave folder exists, if not create it, if yes delete it and create it again
    if os.path.exists(local_gsdk_path + "protocol/z-wave/ZWave/lib"):
        shutil.rmtree(local_gsdk_path + "protocol/z-wave/ZWave/lib")
    os.makedirs(local_gsdk_path + "protocol/z-wave/ZWave/lib")
    print("libzwave folder created")

    #check if libzpal folder exists, if not create it, if yes delete it and create it again
    if os.path.exists(local_gsdk_path + "protocol/z-wave/platform/SiliconLabs/PAL/lib"):
        shutil.rmtree(local_gsdk_path + "protocol/z-wave/platform/SiliconLabs/PAL/lib")
    os.mkdir(local_gsdk_path + "protocol/z-wave/platform/SiliconLabs/PAL/lib")
    print("libzpal folder created")

    #check if bootloader folder exists, if not create it, if yes delete it and create it again
    if os.path.exists(local_gsdk_path + "protocol/z-wave/Apps/bin"):
        shutil.rmtree(local_gsdk_path + "protocol/z-wave/Apps/bin")
    os.mkdir(local_gsdk_path + "protocol/z-wave/Apps/bin")
    print("bootloader folder created")
    
def main():

    #parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--build", help="build number", required=True)
    parser.add_argument("-br", "--branch", help="branch name", default='develop/24q2')
    args = parser.parse_args()
    
    build_number = args.build
    branch = args.branch
    
    handle_environment_before_download()

    start_time = time.time()
    download_rail_artifacts(build_number, branch)
    download_nvm3_artifacts(build_number, branch)
    download_ZW_libs(build_number, branch)
    download_ZPAL_libs(build_number, branch)
    download_bootloaders(build_number, branch)
    # time taken for the script to run
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()
