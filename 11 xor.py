# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 00:36:50 2023

@author: bagul
"""

string = "Hello World"

# AND operation with 127
and_result = ''.join(chr(ord(char) & 127) for char in string)
print("AND result:", and_result)

# XOR operation with 127
xor_result = ''.join(chr(ord(char) ^ 127) for char in string)
print("XOR result:", xor_result)



string = "Hello World"

# Convert the string to a list
char_list = list(string)
for i in range(len(char_list)):
    char_list[i] = chr(ord(char_list[i]) | 127)

# Convert the modified list back to a string
modified_string = ''.join(char_list)

# Display the modified string
print(modified_string)