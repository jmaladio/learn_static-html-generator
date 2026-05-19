import unittest

from nodes.htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("li", "Item A")
        node2 = HTMLNode("li", "Item A")
        self.assertEqual(node.tag, node2.tag)
        self.assertEqual(node.value, node2.value)
        self.assertEqual(node.children, node2.children)
        self.assertEqual(node.props, node2.props)

    def test_not_eq(self):
        node = HTMLNode("li", "Item A")
        node2 = HTMLNode("li", "Item B")
        self.assertEqual(node.tag, node2.tag)
        self.assertNotEqual(node.value, node2.value)
        self.assertEqual(node.children, node2.children)
        self.assertEqual(node.props, node2.props)
    
    def test_plain_text(self):
        node = HTMLNode(value = "This is plain text")
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, "This is plain text")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

if __name__ == "main":
    unittest.main()