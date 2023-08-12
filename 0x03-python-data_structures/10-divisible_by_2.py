
def divisible_by_2(my_list=[]):
    new = []
    for i in my_list:
        temp = False if i%2 == 1 else True
        new.append(temp)
    return new

