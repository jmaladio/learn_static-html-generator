import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_p_with_attr(self):
        node = LeafNode("p", "Hello, world!", {"attr": "value"})
        self.assertEqual(node.to_html(), "<p attr=\"value\">Hello, world!</p>")