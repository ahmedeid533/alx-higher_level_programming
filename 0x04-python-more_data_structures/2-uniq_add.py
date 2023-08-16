#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = []
    for i in my_list:
        if i not in uniq:
            uniq.append(i)
    summ = 0
    for j in uniq:
        summ += j
    return summ
