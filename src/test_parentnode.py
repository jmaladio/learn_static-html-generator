import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    def test_to_html_with_multiple_children(self):
        child_nodeA = LeafNode("h1", "A title")
        child_nodeB = LeafNode("p", "A paragraph")
        parent_node = ParentNode("div", [child_nodeA, child_nodeB])
        self.assertEqual(parent_node.to_html(), "<div><h1>A title</h1><p>A paragraph</p></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_no_children(self):
        parent_nodeA = ParentNode("div", None)
        parent_nodeB = ParentNode("div", [])
        self.assertRaises(ValueError, parent_nodeA.to_html)
        self.assertRaises(ValueError, parent_nodeB.to_html)