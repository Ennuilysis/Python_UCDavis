import copy
from typing import Optional, Callable, TypeVar, Generic

from Trees.src.errors import MissingValueError, EmptyTreeError
from Trees.src.nodes.bst_node import BSTNode

T = TypeVar('T')
K = TypeVar('K')


class BST(Generic[T, K]):
    """
    T: The value stored in the node
    K: The value used in comparing nodes
    """

    def __init__(self, root: Optional[BSTNode[T]] = None, key: Optional[Callable[[T], K]] = lambda x: x) -> None:
        # key= The function to be applied to a node's value for comparison purposes.
        self.root = root
        self.key = key

    def find_height(self, tree_node: BSTNode) -> int:
        # print(node.value, cur_h)
        if type(tree_node) != BSTNode:
            return -1
        left_H = self.find_height(tree_node.left)
        right_H = self.find_height(tree_node.right)
        return 1 + max(left_H, right_H)

    @property
    def height(self) -> int:
        if self.root != BSTNode:
            return -1
        return self.find_height(self.root)

    def check_tree(self) -> None:
        if type(self.root) != BSTNode:
            raise EmptyTreeError

    def __len__(self) -> int:
        num_node: int = 0
        if type(self.root) != BSTNode:
            return 0

        def count(node):
            nonlocal num_node
            if type(node) == BSTNode:
                num_node += 1
                for x in node:
                    count(x)

        count(self.root)
        return num_node

    # the value of a node is whatever is instanced as value of the node. It is not processed by the key.
    # Comparisons use the key.
    def become_leaf(self, value, node):
        if type(value) == BSTNode:
            val_k: int = self.key(value.value)
        else:
            val_k = self.key(value)
        node_k: int = self.key(node.value)
        if val_k > node_k:
            if type(node.right) == None:
                if type(value) == BSTNode:
                    node.right = value
                else:
                    node.right = BSTNode(value, parent=node)
            else:
                self.become_leaf(value, node.right)
        elif val_k < node_k:
            if node.left == None:
                if type(value) == BSTNode:
                    node.left = value
                else:
                    node.left = BSTNode(value, parent=node)
            else:
                self.become_leaf(value, node.left)
        elif val_k == node_k:
            if node.right == None:
                node.right = BSTNode(value, parent=node)
            else:
                ting = BSTNode(value, parent=node)
                ting.right = node.right
                node.right.parent = ting
                node.right = ting

    def add_value(self, value: T) -> None:
        if self.root == None:
            self.root = BSTNode(value)
        else:
            self.become_leaf(value, self.root)

    def hunt_node(self, value, node) -> BSTNode:
        val_k = self.key(value)
        node_k = self.key(node.value)
        if node.value == value:
            return node
        elif val_k > node_k:
            if node.right == None:
                raise MissingValueError
            else:
                return self.hunt_node(value, node.right)
        elif val_k < node_k:
            if node.left == None:
                raise MissingValueError
            else:
                return self.hunt_node(value, node.left)

    def get_node(self, value: K) -> BSTNode[T]:
        """
                Get the node with the specified value
                :param value:
                :raises MissingValueError if there is no node with the specified value
                :return:
                """
        outcome: BSTNode = self.hunt_node(value, self.root)
        return outcome

    def get_max_node(self, start_node=None) -> BSTNode[T]:
        self.check_tree()
        if start_node == None:
            node = self.root
        else:
            node = start_node
        while node.right != None:
            node = node.right
        return node

    def get_min_node(self, start_node=None) -> BSTNode[T]:
        """
        Return the node with the smallest value in the BST
        :return:
        """
        if start_node == None:
            node = self.root
        else:
            node = start_node
        self.check_tree()
        while node.left != None:
            node = node.left
        return node

    def helper_remove(self, target: BSTNode, successor: BSTNode, L_o_R, t_more_than_p: bool):
        # if L_o_R is l, then that means the successor is the left child of the target.
        # if L_O_R is r, that means the successor is the right child.
        # t_more_than_p is a true false. If true, than the target is the right child of its parent.
        # successor assignment
        if t_more_than_p:  # target more than parent
            target.parent.right = successor  # the sucessor of the target becomes targets parents child
        else:
            target.parent.left = successor
        if L_o_R == 'r':  # the successor is greater than the target
            temp_node: BSTNode = self.get_min_node(
                successor.left)  # find the min node of the left of the successor, with no left child.
            temp_node.left = target.left  # that min node inherits the targets left children.
            target.left.parent = temp_node  # the targets first left child becomes the successors leftmost childs left child.
        elif L_o_R == 'l':
            temp_node: BSTNode = self.get_max_node(
                successor.right)  # find the max node of the right of the successor, with no right child.
            self.add_value(target.right)  # that max node inherits the targets right children.
            target.right.parent = temp_node  # the targets first right child becomes the successors rightmost child's right child.
        successor.parent = target.parent

    def remove_value(self, value: K) -> None:
        """
        Remove the node with the specified value.
        When removing a node with 2 children take the successor for that node
        to be the largest value smaller than the node (the max of the
        left subtree)
        :param value:
        :return:
        :raises MissingValueError if the node does not exist
        """
        target: BSTNode = self.get_node(value)

        if target == None:
            raise MissingValueError
        if target.parent == None:
            self.root = None
            return
        elif target.parent.right == target:
            target_more_than_parent = True
        else:
            target_more_than_parent = False
        if target.parent == None and target.left == None and target.right == None:
            self.root = None
        elif target.left == None and target.right == None:
            if target_more_than_parent:
                target.parent.right = None
            elif not target_more_than_parent:
                target.parent.left = None
        elif target.left == None and target.right != None:
            if target_more_than_parent:
                target.parent.right = target.right
            else:
                target.parent.left = target.right
        elif target.left != None and target.right == None:
            if target_more_than_parent:
                target.parent.right = target.right
            else:
                target.parent.left = target.right
        else:
            val_k = self.key(value)
            right_val: BSTNode = self.get_min_node(target.right)  # will always be a leaf node
            left_val: BSTNode = self.get_max_node(target.left)  # will always be a leaf node.
            target_V_left: int = abs(val_k - self.key(left_val.value))
            target_V_right: int = abs(target.value - self.key(right_val.value))
            if target_V_left <= target_V_right:
                self.helper_remove(target, target.left, "l", target_more_than_parent)
            else:
                self.helper_remove(target, target.right, "r", target_more_than_parent)

    def __eq__(self, other: object) -> bool:
        if self is other:
            return True
        elif isinstance(other, BST):
            if len(self) == 0 and len(other) == 0:
                return True
            else:
                return len(self) == len(other) and self.root.value == other.root.value and \
                       BST(self.root.left) == BST(other.root.left) and \
                       BST(self.root.right) == BST(other.root.right)
        else:
            return False

    def __ne__(self, other: object) -> bool:
        return not (self == other)

    def __deepcopy__(self, memodict) -> "BST[T,K]":
        """
        I noticed that for some tests deepcopying didn't
        work correctly until I implemented this method so here
        it is for you
        :param memodict:
        :return:
        """
        new_root = copy.deepcopy(self.root, memodict)
        new_key = copy.deepcopy(self.key, memodict)
        return BST(new_root, new_key)
