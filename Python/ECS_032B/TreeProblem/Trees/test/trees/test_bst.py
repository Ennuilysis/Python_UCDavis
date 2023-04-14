import unittest
from Trees.src.trees.bst_tree import BST
from Trees.src.nodes.bst_node import BSTNode


class TestBST(unittest.TestCase):
    def test_min_node(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(200)
        tree.add_value(90)
        tree.add_value(70)
        tree.add_value(250)
        self.assertEqual(tree.root.left.left,tree.get_min_node())

    def test_get_node(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(200)
        tree.add_value(90)
        tree.add_value(70)
        tree.add_value(250)
        self.assertEqual(tree.root.right.right,tree.get_node(250))

    def test_duplicate_insert(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(200)
        tree.add_value(90)
        tree.add_value(70)
        tree.add_value(250)
        tree.add_value(100)

        root = BSTNode(100)
        root.left = BSTNode(80)
        root.right = BSTNode(100)
        root.right.right = BSTNode(200)
        root.right.right.right=BSTNode(250)
        root.left.left = BSTNode(70)
        root.left.right = BSTNode(90)
        cmp_tree = BST(root)
        self.assertEqual(cmp_tree, tree)


    def test_max_node(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(200)
        tree.add_value(90)
        tree.add_value(70)
        tree.add_value(250)


        self.assertEqual(tree.root.right.right,tree.get_max_node())

    def test_create_empty_tree111111(self):
        tree = BST()
        self.assertEqual(len(tree), 0)
        self.assertIsNone(tree.root)
        self.assertEqual(tree.height, -1)

    def test_create_empty_tree(self):
        tree = BST()
        self.assertEqual(len(tree), 0)
        self.assertIsNone(tree.root)

    def test_create_tree(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(200)
        tree.add_value(90)
        tree.add_value(70)

        root = BSTNode(100)
        root.left = BSTNode(80)
        root.right = BSTNode(200)
        root.left.left = BSTNode(70)
        root.left.right = BSTNode(90)
        cmp_tree = BST(root)
        self.assertEqual(tree, cmp_tree)

    def test_get_node_chr(self):
        tree = BST()
        tree.add_value("Hi")
        tree.add_value("apples")
        tree.add_value("tell")
        tree.add_value("90")
        tree.add_value("70")
        #"apples">"Hi" is True
        self.assertEqual(tree.get_node("apples"), tree.root.right)

    def test_create_tree111111(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(200)
        tree.add_value(90)
        tree.add_value(70)
        root = BSTNode(100)
        root.left = BSTNode(80)
        root.right = BSTNode(200)
        root.left.left = BSTNode(70)
        root.left.right = BSTNode(90)
        cmp_tree = BST(root)
        self.assertEqual(tree, cmp_tree)
        self.assertEqual(tree.height, cmp_tree.height)

    def test_create_tree_chr(self):
        tree = BST()
        tree.add_value("Hi")
        tree.add_value("8")
        tree.add_value("tell")
        tree.add_value("90")
        tree.add_value("70")
        root = BSTNode("Hi")
        root.left = BSTNode("8")
        root.right = BSTNode("tell")
        root.left.left = BSTNode("70")
        root.left.right = BSTNode("90")
        cmp_tree = BST(root)
        self.assertEqual(tree, cmp_tree)
        self.assertEqual(tree.height, cmp_tree.height)

    def test_tree_not_eq_chr(self):
        tree = BST()
        tree.add_value("Hi")
        tree.add_value("8")
        tree.add_value("tell")
        tree.add_value("90")
        tree.add_value("70")
        root = BSTNode("Hi")
        root.left = BSTNode("2")
        root.right = BSTNode("tell")
        root.left.left = BSTNode("90")
        root.left.right = BSTNode("70")
        cmp_tree = BST(root)
        self.assertNotEqual(tree, cmp_tree)

    def test_tree_not_eq(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(200)
        tree.add_value(90)
        tree.add_value(70)

        root = BSTNode(100)
        root.left = BSTNode(80)
        root.right = BSTNode(200)
        root.left.left = BSTNode(70)
        root.left.right = BSTNode(92)

        cmp_tree = BST(root)
        cmp_tree._num_nodes = 5
        self.assertNotEqual(tree, cmp_tree)

    def test_del_node_with_len(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(200)
        tree.add_value(90)
        tree.add_value(70)
        tree.add_value(250)
        tree.remove_value(250)
        output = len(tree)
        self.assertEqual(5, output)
        tree.remove_value(80)
        self.assertEqual(4,len(tree))

    def test_tree_organize_after_remove_node(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(200)
        tree.add_value(90)
        tree.add_value(70)
        tree.add_value(250)
        tree.remove_value(250)
        tree.remove_value(80)

        root = BSTNode(100)
        root.left = BSTNode(70)
        root.right = BSTNode(200)
        root.left.right = BSTNode(90)
        cmpr_tree=BST(root)
        self.assertEqual(tree,cmpr_tree)

    def test_len_of_bst(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(200)
        tree.add_value(90)
        tree.add_value(70)
        tree.add_value(250)
        tree.add_value(800)
        tree.add_value(1)
        tree.add_value(85)
        tree.remove_value(80)
        self.assertEqual(len(tree), 8)

    def test_height_Prop_of_bst(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(200)
        tree.add_value(90)
        tree.add_value(70)
        tree.add_value(250)
        tree.add_value(800)
        tree.add_value(1)
        self.assertEqual(tree.height, 3)

    def test_mega_test(self):
        #Just see if it runs
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(200)
        tree.add_value(90)
        tree.add_value(70)
        tree.add_value(250)
        tree.add_value(800)
        tree.add_value(1)
        tree.add_value(104)
        tree.add_value(84)
        tree.add_value(204)
        tree.add_value(86)
        tree.add_value(64)
        tree.add_value(257)
        tree.add_value(799)
        tree.add_value(1)
        tree.remove_value(1)
        tree.add_value(1)


#TADAH. Tree works.

if __name__ == '__main__':
    unittest.main()
