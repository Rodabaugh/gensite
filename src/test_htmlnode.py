import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_href_props(self):
        node = HTMLNode("a", "A link", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_tohtml(self):
        node = LeafNode("a", "A link", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank">A link</a>')

    def test_ParentNode(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_NestedParentNode(self):
        node = ParentNode(
            "p",
            [
                ParentNode(
                    "b",
                [
                    LeafNode("i", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text")
                ],
                )
            ],
        )

        self.assertEqual(node.to_html(), "<p><b><i>Bold text</i>Normal text<i>italic text</i>Normal text</b></p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

    def test_ChildlessParentNode(self):
        node = ParentNode("p",None,)
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()