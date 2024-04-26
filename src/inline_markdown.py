from textnode import *
import re

def split_nodes_delimiter(nodes, delimiter, text_type):
    new_nodes = []
    for node in nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        split_nodes = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown - a section was not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(nodes):
    new_nodes = []
    for node in nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        node_text = node.text
        images = extract_markdown_images(node_text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        for image in images:
            sections = node_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown: image section is not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(
                TextNode(image[0], text_type_image, image[1])
            )
            node_text = sections[1]
        if node_text != "":
            new_nodes.append(TextNode(node_text, text_type_text))
    return new_nodes

def split_nodes_link(nodes):
    new_nodes = []
    for node in nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        node_text = node.text
        links = extract_markdown_links(node_text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        for link in links:
            sections = node_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section is not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            node_text = sections[1]
        if node_text != "":
            new_nodes.append(TextNode(node_text, text_type_text))
    return new_nodes