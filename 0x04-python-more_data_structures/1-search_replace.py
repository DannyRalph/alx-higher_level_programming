#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for i in range(len(new_list)):
        if new_list[i] == search:
            m = i + 1
            new_list.insert(i, replace)
            new_list.remove(new_list[m])
    return (new_list)
