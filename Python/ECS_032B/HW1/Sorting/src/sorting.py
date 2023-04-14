import sys
from typing import Iterable, List, TypeVar, Any

T = TypeVar('T')

swap(1,2,3)

def swap(values: List, index1: int, index2: int) -> None:
    #list(values, index1, index2)

    #use list to translate other object types to list.
    #translation will create entire new object.
    """
    Swap the elements at index1 and index in values
    :param values: a list
    :param index1: the position of the first element in values to swap
    :param index2: the position of the second element in values to swap
    :return: None
    """
    a = int(values[index1])
    b = int(values[index2])
    values[index1]=b
    values[index2]=a

    #ok. so the error should be that index values arent actually changed. Theres no output, no new list. Instead,
    #output should not be None, but rather a integer list. Then remove lines 17 to 19. Replace them with the following.
    #values[index1]=b
    #values[index2]=a
    #Documentation does say the return should be none. But within the function, objective is not achieved.


def get_index_of_min_item(items: List[T], start: int = 0) -> int:
    """
    Locate the index of the minimum item in items beginning at start
    :param items: The items to search
    :return: The index of the smallest item in items
    """
    #start needs to +1 for every call
    print("start",start)
    min_item = items[start]
    for index in range(len(items)): #ok. For loop of every item, but made mistake of adding 1.////
        #should be range(len(items)), so (0:len(items))
        cur_item = items[index] #ok. sets current item.
        if cur_item < min_item: #ok. checks wether the current item is lareger than min. Error was operator.
            #Should instead have less than min.
            ind_min= index  #if current item bigger, then the inde of the min item will be current index.
            min_item = cur_item         #if current item bigger, then minimum item will become curent item? what?
    return ind_min #the original program returned the minimum value, not the index.
    #For some reason, everything in get_index_of_min works, and so does sort items.

def sort_items(items: Iterable[T]) -> List[T]: #give me some iterable, were all iterables are same
    #give back a list of strings
    #give back a reference list, or a deep copies.
    Items=list(items)
    """
    Give back a NEW sorted list of the items.
    We do this by finding the ith smallest item and swapping it into position i in the list
    :param items: The items to sort. This variable should not be modified
    :return: A sorted list of the items
    """
    start=0
    for pos, item in enumerate(Items):
        ind_min = get_index_of_min_item(Items,start) #for each loop iteration, the minimum of items is found.
        swap(Items, pos, ind_min) #Original didn't include list two swap within, and didnt use index input.
        # Then after indexing min item, the index is never used. Instead, the position,
        # or value of current iteration, is used to swap the location of the current iterated item, and an item in
        # the list.
        start+=1
        print(Items)
    return Items #this is correct

#