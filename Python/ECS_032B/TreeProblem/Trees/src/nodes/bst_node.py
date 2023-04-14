import copy
from typing import Generic, Iterable, TypeVar, Optional, Union,List

T = TypeVar('T')


class BSTNode(Generic[T]):
    """
    Your node should permit at least the following
    node.left: get the left child
    node.right: get the right child
    """

    def __init__(self, value: T, children: Optional[List["BSTNode[T]"]] = None,
                 parent: Optional["BSTNode[T]"] = None) -> None:
        # children[1] is the right node, children[0] is the left node.
        self.value = value
        if children == None:
            self.left: Union[None, "BSTNode"] = None
            self.right: Union[None, "BSTNode"] = None
        else:
            self.left = children[0]
            self.right = children[1]
        self.parent: Union[None, "BSTNode"] = parent

    def __iter__(self) -> Iterable["BSTNode[T]"]:
        if self.left is not None:
            yield self.left
        if self.right is not None:
            yield self.right

    # when I do for x in BST node what I return here will be iterated through

    def __deepcopy__(self, memodict) -> "BSTNode[T]":
        """
        I noticed that for some tests deepcopying didn't
        work correctly until I implemented this method so here
        it is for you
        :param memodict:
        :return:
        """
        copy_node = BSTNode(copy.deepcopy(self.value, memodict))
        copy_node.left = copy.deepcopy(self.left, memodict)
        copy_node.right = copy.deepcopy(self.right, memodict)
        copy_node.parent = copy.deepcopy(self.parent, memodict)
        return copy_node

    def __str__(self):
        return self.__dict__

    def __eq__(self, other:"BSTNode")->bool:
        if type(self)!=type(other):
            return False
        elif self.value==other.value:
            return True
        else:
            return False
