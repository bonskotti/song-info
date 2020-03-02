#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 23:37:39 2020

@author: bonskotti
"""

def get_data_path():
    """
    Finds out the path of the data-file.

    Returns
    -------
    Path of the data-file.

    """
    
    import os
    import sys
    
    script_dir = sys.path[0]
    return os.sep.join([script_dir, 'data', 'data.json'])


def get_data():
    """
    Gets the API-key and username out of the json file.

    Returns
    -------
    API-key,username(tuple)

    """
    
    import json
    
    # get the file
    data_path = get_data_path()
    data_file = open(data_path, 'r')
    data_json = data_file.read()
    data_dict = json.loads(data_json)
    
    # get the values out
    api_key = data_dict['api_key']
    username = data_dict['user']
    
    return (api_key,username)
    
    

