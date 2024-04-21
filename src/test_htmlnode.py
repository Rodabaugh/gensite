import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_href_props(self):
        node = HTMLNode("a", "A link", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_tohtml(self):
        node = LeafNode("a", "A link", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank">A link</a>')

if __name__ == "__main__":
    unittest.main()