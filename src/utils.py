from textnode import TextNode, TextType
from leafnode import LeafNode

import re

def text_node_to_html_node(text_node):
    if (text_node.text_type == TextType.TEXT):
        return LeafNode(None, value = text_node.text)
    elif (text_node.text_type == TextType.BOLD):
        return LeafNode("b", text_node.text)
    elif (text_node.text_type == TextType.ITALIC):
        return LeafNode("i", text_node.text)
    elif (text_node.text_type == TextType.CODE):
        return LeafNode("code", text_node.text)
    elif (text_node.text_type == TextType.LINK):
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif (text_node.text_type == TextType.IMAGE):
        return LeafNode(tag = "img", value = "", props = {"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Invalid Text Type: {text_node.text_type}")
    
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for orig_node in old_nodes:
        if orig_node.text_type != TextType.TEXT:
            new_nodes.append(orig_node)
            continue

        text_splits = orig_node.text.split(delimiter)
        if len(text_splits) % 2 == 0:
            raise ValueError("Invalid markdown syntax")
        
        for i, text_split in enumerate(text_splits):
            if i % 2 == 0:
                new_nodes.append(TextNode(text_split, TextType.TEXT))
            else:
                new_nodes.append(TextNode(text_split, text_type))


    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return [(match[0], match[1]) for match in matches]


def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return [(match[0], match[1]) for match in matches]
