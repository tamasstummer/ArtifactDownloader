import requests
import json
import re
from requests.auth import HTTPBasicAuth
import os

def get_latest_build_number_from_branch(branch_name):
    # Artifactory details
    ARTIFACTORY_URL = 'https://artifactory.silabs.net/artifactory/api/search/aql'
    REPO = 'gsdk-generic-development'
    PATH = f'{branch_name}'

    # Artifactory credentials
    USERNAME = 'user'
    PASSWORD = 'pass'

    # Construct the AQL Query
    # Dont indent this otherwise it wont work
    aql_query = """
items.find({"repo": "%s", "path": {"$match": "%s/*"}, "name": {"$match": "*.zip"}}).sort({"$desc": ["created"]}).limit(1)
""" % (REPO, PATH)

    # Execute the AQL query
    try:
        response = requests.post(
            ARTIFACTORY_URL,
            data=aql_query,
            headers={'Content-Type': 'text/plain'},
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
            verify=False  # verify=False for demo purposes
        )

        if response.status_code == 200:
            results = json.loads(response.text)
            if results['results']:
                latest_artifact_path = results['results'][0]['path']
                # Extract the build number from the path
                build_number_match = re.search(r'/(\d+)/', latest_artifact_path)
                if build_number_match:
                    build_number = build_number_match.group(1)
                    print(f"Latest build number: {build_number} on branch: {branch_name}")
                    return build_number
                else:
                    print("Build number not found in the path.")
                    os._exit(1)
                    return None
            else:
                print("No artifacts found.")
                return None
        else:
            print(f"Failed to query Artifactory: {response.status_code}, {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def download_rail_artifacts(build_number, branch_name):

    rail_libs = [
    "librail_config_zgm130s037hgn1_gcc.a",
    "librail_config_zgm130s037hgn_gcc.a",
    "librail_config_zgm230sa27hgn_gcc.a",
    "librail_config_zgm230sa27hnn_gcc.a",
    "librail_config_zgm230sa27hnn_jar.a",
    "librail_config_zgm230sb27hgn_gcc.a",
    "librail_module_efr32xg12_gcc_release.a",
    "librail_module_efr32xg13_gcc_release.a",
    "librail_module_efr32xg14_gcc_release.a",
    "librail_module_efr32xg1_gcc_release.a",
    "librail_module_efr32xg21_gcc_release.a",
    "librail_module_efr32xg22_gcc_release.a",
    "librail_module_efr32xg23_gcc_release.a",
    "librail_module_efr32xg24_gcc_release.a",
    "librail_module_efr32xg25_gcc_release.a",
    "librail_module_efr32xg26_gcc_release.a",
    "librail_module_efr32xg27_gcc_release.a",
    "librail_module_efr32xg28_gcc_release.a",
    "librail_efr32xg12_gcc_release.a",
    "librail_efr32xg13_gcc_release.a",
    "librail_efr32xg14_gcc_release.a",
    "librail_efr32xg1_gcc_release.a",
    "librail_efr32xg21_gcc_release.a",
    "librail_efr32xg22_gcc_release.a",
    "librail_efr32xg23_gcc_release.a",
    "librail_efr32xg24_gcc_release.a",
    "librail_efr32xg25_gcc_release.a",
    "librail_efr32xg26_gcc_release.a",
    "librail_efr32xg27_gcc_release.a",
    "librail_efr32xg28_gcc_release.a"
    ]

    # Create the folder structure first
    os.system(f"mkdir autogen")
    


    for lib in rail_libs:
        url = f"http://iot-jenkins-master.silabs.com:8080/job/Gecko_SDK_Suite_RAIL_Continuous_Integration/job/{branch_name}/{build_number}/artifact/super/platform/radio/rail_lib/autogen/librail_release/{lib}"
        print(url)
        os.system(f"wget {url} -O {lib}")





def main():
    branch = 'develop/24q2'
    build_number = get_latest_build_number_from_branch(branch)
    download_rail_artifacts(build_number, branch)


if __name__ == "__main__":
    main()
