from textnode import TextNode
from htmlnode import *

def main():
    test_node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(test_node)

if __name__ == "__main__":
    main()

def text_node_to_html_node(text_node):
    support_types = ["text", "bold", "italic", "code", "link", "image"]

    if text_node.type not in support_types:
        raise Exception("Unsupported Type")
    
    if text_node.type == "text":
        return LeafNode(None, text_node.text)
    elif text_node.type == "bold":
        return LeafNode("b", text_node.text)
    elif text_node.type == "italic":
        HTMLNode("i", text_node.text)
    elif text_node.type == "code":
        HTMLNode("code", text_node.text)
    elif text_node.type == "link":
        HTMLNode("a", text_node.text, None, f'href={text_node.url}')
    elif text_node.type == "image":
        HTMLNode("img", "", None, f'src="{text_node.url}" alt="{text_node.text}"')