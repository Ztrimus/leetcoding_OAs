'''
-----------------------------------------------------------------------
File: TP/sha256_hash.py
Creation Time: Jul 21st 2024, 6:49 pm
Author: Saurabh Zinjad
Developer Email: saurabhzinjad@gmail.com
Copyright (c) 2023-2024 Saurabh Zinjad. All rights reserved | https://github.com/Ztrimus
-----------------------------------------------------------------------
'''

import hashlib

def sha256_hash(input_string):
    if not isinstance(input_string, str):
        raise ValueError("input is invalid type")   
    
    # Encode the string to bytes, then compute the hash
    sha256 = hashlib.sha256()
    sha256.update(input_string.encode('utf-8'))
    
    # Return the hexadecimal representation of the hash
    sha256_code = sha256.hexdigest()
    return sha256_code

# Example usage
input_string = "query: routeInfo" # Replace this with actual value you get after reverse engineering the api in the curl command below.You're required to submit this input_string value in google forms
# input_string = "26c6f9703c762620476c83cea0122d31c7ab15b9a949aaae1cb933dcfc832ed0" # Replace this with actual value you get after reverse engineering the api in the curl command below.You're required to submit this input_string value in google forms
print(f"SHA-256 hash: {sha256_hash(input_string)}")
