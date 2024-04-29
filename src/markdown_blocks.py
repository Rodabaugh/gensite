from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node
import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ulist = "unordered_list"
block_type_olist = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    final_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        final_blocks.append(block)
    return final_blocks

def block_to_block_type(block):
    block_lines = block.split("\n")

    if(
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
       ):
        return block_type_heading
    if len(block_lines) > 1 and block_lines[0].startswith("```") and block_lines[-1].startswith("```"):
        return block_type_code
    if block.startswith(">"):
        for line in block_lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if block.startswith("* "):
        for line in block_lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("- "):
        for line in block_lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("1. "):
        i = 1
        for line in block_lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_olist
    return block_type_paragraph

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)
    return children

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError(f"Invalid Markdown/Invalid Quote:\n\n{line}")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def ulist_to_html_node(block):
    block_lines = block.split("\n")
    html_blocks = []
    for line in block_lines:
        text = line[2:]
        children = text_to_children(text)
        html_blocks.append(ParentNode("li", children))
    return ParentNode("ul", html_blocks)

def olist_to_html_node(block):
    block_lines = block.split("\n")
    html_blocks = []
    for line in block_lines:
        text = line[3:]
        children = text_to_children(text)
        html_blocks.append(ParentNode("li", children))
    return ParentNode("ol", html_blocks)

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def heading_to_html_node(block):
    heading_level = 0

    for i in range(1,7):
        if block.startswith("#" * i + " "):
            heading_level = i
            break

    if heading_level == 0:
        raise ValueError(f"Invalid heading: This input is not a heading.\n\n{block}")

    text = block[heading_level + 1 :]
    children = text_to_children(text)

    return ParentNode("h" + str(heading_level), children)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == block_type_paragraph:
            html_nodes.append(paragraph_to_html_node(block))
        elif block_type == block_type_heading:
            html_nodes.append(heading_to_html_node(block))
        elif block_type == block_type_code:
            html_nodes.append(code_to_html_node(block))
        elif block_type == block_type_quote:
            html_nodes.append(quote_to_html_node(block))
        elif block_type == block_type_ulist:
            html_nodes.append(ulist_to_html_node(block))
        elif block_type == block_type_olist:
            html_nodes.append(olist_to_html_node(block))
        else:
            raise ValueError(f"An unsupported block type was encountered in block:\n\n{block}")
    
    return ParentNode("div", children=html_nodes)