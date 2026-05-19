from email.mime import image

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

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        processed_nodes = []
        text_to_process = node.text
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_nodes.append(node)
        else:
            for image_alt, image_link in images:
                sections = text_to_process.split(f"![{image_alt}]({image_link})", 1)
                if len(sections[0]) != 0:
                    processed_nodes.append(TextNode(sections[0], TextType.TEXT))
                processed_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
                text_to_process = sections[1]
            if len(text_to_process) != 0:
                    processed_nodes.append(TextNode(text_to_process, TextType.TEXT))
            
            new_nodes.extend(processed_nodes)
            
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        processed_nodes = []
        text_to_process = node.text
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            new_nodes.append(node)
        else:
            for link_text, link_url in links:
                sections = text_to_process.split(f"[{link_text}]({link_url})", 1)
                if len(sections[0]) != 0:
                    processed_nodes.append(TextNode(sections[0], TextType.TEXT))
                processed_nodes.append(TextNode(link_text, TextType.LINK, link_url))
                text_to_process = sections[1]
            if len(text_to_process) != 0:
                    processed_nodes.append(TextNode(text_to_process, TextType.TEXT))
            
            new_nodes.extend(processed_nodes)

    return new_nodes

def text_to_textnodes(text):

    bold_text_nodes = split_nodes_delimiter([TextNode(text, TextType.TEXT)], "**", TextType.BOLD)
    italic_text_nodes = split_nodes_delimiter(bold_text_nodes, "*", TextType.ITALIC)
    code_text_nodes = split_nodes_delimiter(italic_text_nodes, "`", TextType.CODE)
    image_text_nodes = split_nodes_image(code_text_nodes)
    link_text_nodes = split_nodes_link(image_text_nodes)

    return link_text_nodes