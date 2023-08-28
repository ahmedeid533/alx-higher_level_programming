
def safe_print_list(my_list=[], x=0):
    j = 0
    try:
        for i in range(x):
            print(my_list[i],end="")
            j+=1 
    except: 
        o = 0
    print("")
    return j
my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
