from Trees.src.nodes.bst_node import BSTNode
from Trees.src.trees.bst_tree import BST
from Trees.src.donor_prog.donor import Donor
from Trees.src.errors import MissingValueError, EmptyTreeError
from typing import List, Union
import sys, copy

# load file
donor_tree = BST(None, key=lambda x: x.donor_val)


def pheonix():
    """Deep copy was being too weird"""
    global donor_tree
    donor_tree = BST(None, key=lambda x: x.donor_val)
    with open(sys.argv[1], "r") as file:
        for line in file:
            donor_tree.add_value(value=Donor(line.split(" : ")))


pheonix()


def _all():
    """Print all of the donors from the smallest donation amount to the largest donation amount"""
    while len(donor_tree) > 0:
        max_NODE = donor_tree.get_max_node()
        print(max_NODE.value)
        donor_tree.remove_value(max_NODE.value)
    pheonix()


def cheap():
    min_node: BSTNode = donor_tree.get_min_node()
    print(min_node.value)


def rich():
    max_node: BSTNode = donor_tree.get_max_node()
    print(max_node.value)


def who(sign, val):
    """who amount: Prints the first donor that who donated amount if any
    who +amount: Prints the first donor that donated at least amount if any
    who -amount: Prints the first donor that donated no more than amount if any"""
    try:
        tree_node = donor_tree.get_node(val)
        print(tree_node.value)
        return
    except MissingValueError:
        pass
    Node_save: Union[BSTNode, None] = None
    if sign == "-":
        while len(donor_tree) > 0:
            tree_node: BSTNode = donor_tree.get_min_node()
            cur_val: int = val - donor_tree.key(tree_node.value)
            Node_val: int = donor_tree.key(Node_save.value)
            if Node_save == None:
                Node_save = tree_node
            elif cur_val < Node_val:
                Node_save = tree_node
            else:
                break
            donor_tree.remove_value(cur_val)
        pheonix()
    elif sign == '+':
        while len(donor_tree) > 0:
            tree_node = donor_tree.get_max_node()
            cur_val = donor_tree.key(tree_node.value) - val
            if Node_val != None:
                Node_val = donor_tree.key(Node_save.value)
            if Node_save == None:
                Node_save = tree_node
            elif cur_val < Node_val:
                Node_save = tree_node
            else:
                break
            donor_tree.remove_value(cur_val)
        pheonix()
    if Node_save==None:
        print("No Match")
    else:
        print(Node_save.value)


def call_command(str_val: str):
    dict_command = {"all": _all, "who": who, "rich": rich, "cheap": cheap}
    if str_val[0:2] == "who":
        mark: str = str_val[4]
        amount: int = int(str_val[5:])
        who(mark, amount)
    else:
        dict_command[str_val]()


call_command(sys.argv[2])
