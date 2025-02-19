"""
Name: Bin Ni
Email: bin.ni81@myhunter.cuny.edu
Resources: None
"""
from typing import List

def hex_plus_one(digits: List[str]) -> List[str]:
    """
    This function takes a large number stored as a list of hexadecimal digits and returns 
    the large number incremented by 1
    """
    hex_map = {str(i): i for i in range(10)}
    hex_map.update({chr(65 + i): 10 + i for i in range(6)})
    rev_hex_map = {v: k for k, v in hex_map.items()}

    carry = 1
    for i in range(len(digits) - 1, -1, -1):
        new_value = hex_map[digits[i]] + carry
        if new_value < 16:
            digits[i] = rev_hex_map[new_value]
            return digits
        else:
            digits[i] = '0'
            carry = 1
    return ['1'] + digits
