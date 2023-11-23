import re
import os

keywords = [
    'HAI', 'KTHXBYE', 'WAZZUP', 'BUHBYE', 'BTW', 'OBTW', 'TLDR', 'I HAS A',
    'ITZ', 'R', 'SUM OF', 'DIFF OF', 'PRODUKT OF', 'QUOSHUNT OF', 'MOD OF',
    'MOD OF', 'BIGGR OF', 'SMALLR OF', 'BOTH OF', 'EITHER OF', 'WON OF', 'NOT',
    'ANY OF', 'ALL OF', 'BOTH SAEM', 'DIFFRINT', 'SMOOSH', 'MAEK', 'A', 'IS NOW A',
    'VISIBLE', 'GIMMEH', 'O RLY?', 'YA RLY', 'MEBBE', 'NO WAI', 'OIC', 'WTF?', 'OMG',
    'OMGWTF', 'IM IN YR', 'UPPIN', 'NERFIN', 'YR', 'TIL', 'WILE', 'IM OUTTA YR',
    'HOW IZ I', 'IF U SAY SO', 'GTFO', 'FOUND YR', 'I IZ', 'MKAY'
]

def is_keyword(word):
    if word in keywords:
        return 1
    else:
        return 0

string = '''
    HAI
        I HAS A var ITZ 12
        VISIBLE "noot noot" var
    KTHXBYE
'''
strings = string.split("\n")
# for word in string.split():
#     is_keyword(word)