# Developed by Mike Jin
# This scripts check if each project folder already contains the schematic diagram for the job
# and will return a report on all projects that are missing the shcematics, with it's path

import os

#define the root folder where all project folders reside
projects_root = os.getcwd() + "/Sample Data"
#define the target file name
target_name="Schematics.jpg"

def find_missing_schematics(projects_root, target_name):
    """
    Check each immediate subfolder in projects_root for target_name.
    Returns a dict with project folder name as key and its full path as value
    if schematics.jpg is missing.
    """
    missing = {}

    # Loop through each item in the root folder
    for item in os.listdir(projects_root):
        full_path = os.path.join(projects_root, item)
        print("Checking " + item)
        # Check if item is a directory, we will pass for non-directories
        if os.path.isdir(full_path):
            target_path = os.path.join(full_path, target_name)
            #print("checking if "+target_path+" exists")
            # If schematics.jpg is not found, record it
            if not os.path.exists(target_path):
                missing[item] = full_path
    return missing

def print_report(missing_dict):
    """Prints out a report of which project folders are missing Schematics.jpg"""
    if not missing_dict:
        print("✅ All project folders contain Schematics.jpg")
    else:
        print("❌ The following project folders are missing Schematics.jpg:")
        for project, path in missing_dict.items():
            print(f"  • {project}  ->  {path}")

    
projects_missing_schematic = find_missing_schematics(projects_root, target_name)
print_report(projects_missing_schematic)