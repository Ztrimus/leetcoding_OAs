'''
-----------------------------------------------------------------------
File: TP/parallel_hash_full.py
Creation Time: Sep 18th 2024, 11:33 pm
Author: Saurabh Zinjad
Developer Email: saurabhzinjad@gmail.com
Copyright (c) 2023-2024 Saurabh Zinjad. All rights reserved | https://github.com/Ztrimus
-----------------------------------------------------------------------
'''

# Run this script with the following command in the terminal:
# parallel python3 parallel_hash_full.py {1} {2} ::: $(seq 0 100000 308915776) :::+ $(seq 100000 100000 308915776)
# install parallel first

import hashlib
import itertools
import string
import sys

# Character set (lowercase letters)
charset = string.ascii_lowercase

# Target hash provided by the challenge (replace with the actual hash)
target_hash = "14808a5938b5abd9d26fac2f2013d840358d1df123471ee835bde0566672229a"

def generate_string_from_index(index):
    """Generates a 6-character string based on the given index."""
    base = len(charset)
    result = []
    for _ in range(6):
        result.append(charset[index % base])
        index //= base
    return ''.join(result[::-1])

def brute_force_sha256(start_index, end_index):
    """Brute forces the SHA256 hash from start_index to end_index."""
    for index in range(start_index, end_index):
        plain_text = generate_string_from_index(index)
        sha256_hash = hashlib.sha256(plain_text.encode('ascii')).hexdigest()
        if sha256_hash == target_hash:
            print(f"Match found! The plain-text string is: {plain_text}")
            return plain_text
    print(f"No match found in range {start_index} to {end_index}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 parallel_hash_full.py <start_index> <end_index>")
        sys.exit(1)

    # Convert from scientific notation if necessary
    start_index = int(float(sys.argv[1]))  # Convert to float first, then to int
    end_index = int(float(sys.argv[2]))    # Convert to float first, then to int

    brute_force_sha256(start_index, end_index)