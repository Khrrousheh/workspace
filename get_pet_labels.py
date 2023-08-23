#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Mahdi Muhammad Mahdmud Khrrousheh
# DATE CREATED: 16 / August / 2023                                 
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def pet_label_creator(file_name: str) -> str:
    """
    Create the label from the file name under the next rules
        1. Lower case letter
        2. Single space separating each word
        3. Correct representation of the file names from the 10 keys-value pairs
    Parameter:
        file name -> str
    Output:
        res_label -> str
    """
    file_name = file_name.lower()
    name_list = file_name.split("_")
    res_label = ""
    for i in name_list:
        if i.isalpha():
            res_label += i + " "
    res_label = res_label.strip()
    return res_label

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    results_dic = {}
    # function
#     items_in_dic = len(results_dic)
#     print("\nEmpty Dictionary results_dict - n items=",items_in_dic)
    image_dir_list = listdir(image_dir)
    for i in image_dir_list:
        if i not in results_dic.keys():
            results_dic[i] = [pet_label_creator(i)]
        else:
            print("** Warning: Key=", idx, 
               "already exists in results_dic with value =", 
               results_dic[i])

    
    return results_dic
