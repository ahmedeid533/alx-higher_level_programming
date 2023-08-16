
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return None
    romv = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    dicM = {'MMM': 3000, 'MM': 2000, 'M': 1000}
    dicC = {'CM': 900, 'DCCC': 800, 'DCC': 700, 'DC': 600,  'CD': 400, 'D': 500,'CCC': 300,
            'CC': 200, 'C': 100, }
    dicX = {'XC': 90, 'LXXX': 80, 'LXX': 70, 'LX': 60,
             'XL': 40, 'L': 50,'XXX': 30, 'XX': 20, 'X': 10}
    dicI = {'IX': 9, 'VIII': 8, 'VII': 7,  'VI': 6, 'IV': 4, 'V': 5, 
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
    return result


roman_number = "MLXVI"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
