#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [467, 133, 108]
print(validUTF8(data))


data = [240, 188, 128, 167]
print(validUTF8(data))


data = [235, 140]
print(validUTF8(data))



data = [345, 467]
print(validUTF8(data))



data = [250, 145, 145, 145, 145]
print(validUTF8(data))



data = [0, 0, 0, 0, 0, 0]
print(validUTF8(data))


data = []
print(validUTF8(data))

