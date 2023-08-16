#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string or roman_string == None:
        return 0
    dicM = {'MMM': 3000, 'MM': 2000, 'CM': 900, 'M': 1000}
    dicC = {'DCCC': 800, 'DCC': 700, 'DC': 600,  'CD': 400, 'D': 500, 'CCC': 300,
            'CC': 200, 'XC': 90, 'C': 100, }
    dicX = {'LXXX': 80, 'LXX': 70, 'LX': 60,
            'XL': 40, 'L': 50, 'XXX': 30, 'XX': 20, 'IX': 9, 'X': 10}
    dicI = {'VIII': 8, 'VII': 7,  'VI': 6, 'IV': 4, 'V': 5,
            'III': 3, 'II': 2, 'I': 1}
    result = 0
    i = 0
    for k, v in dicM.items():
        if k in roman_string[i:]:
            i += len(k)
            result += v
            break
    for k, v in dicC.items():
        if k in roman_string[i:]:
            i += len(k)
            result += v
            break
    for k, v in dicX.items():
        if k in roman_string[i:]:
            i += len(k)
            result += v
            break
    for k, v in dicI.items():
        if k in roman_string[i:]:
            i += len(k)
            result += v
            break
    return int(result)
