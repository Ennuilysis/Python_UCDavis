import unittest
from Trees.src.nodes.bst_node import BSTNode


class TestBSTNode(unittest.TestCase):
    def test_properties(self):
        test=BSTNode("n",[BSTNode(1),BSTNode(2)],BSTNode("Slappy"))
        self.assertEqual(test.value,"n")
        self.assertEqual(test.right.value,2)
        self.assertEqual(test.left.value,1)
        self.assertEqual(test.parent.value,"Slappy")
    #Professor wrote iterator, so dont need to worry.


if __name__ == '__main__':
    unittest.main()
