from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode


def main():
    text_node = TextNode(
        "This is some anchor text", TextType.LINK, "https://www.boot.dev"
    )
    print(text_node.__repr__())

    html_node = HTMLNode("p", "This is a paragraph", None, { "style": { "color": "blue"} } )
    print(html_node.__repr__())

    leaf_node = LeafNode("p", "This is a paragraph", { "attr": "val" })
    print(leaf_node.__repr__())
main()
