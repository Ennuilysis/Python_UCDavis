import sys
#Find the errors in main and sorting
#in the test files, write code
from src.sorting import sort_items

def main(what) -> None: #missing sys.argv input from command line.
    """
    Sort the integer values passed on the command line and print them out
    :return:
    """

    #sorted_values = sort_items(what)#command sys.argv refers to running
    # the command line paramenters, otherwise configuration parameters.
    #The function imports system arguments, before any arguments are given. No prompt is given from the console.
    print(f'The items we received on the command line are {what}')
    print(f'After sorting them we have {what}')


if __name__ == '__main__':
    main(sys.argv)
