import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def testURLNone(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node, node2)

    def testURLDifferent(self):
        node = TextNode("This is a text node", "bold", "https://erikrodabaugh.com/")
        node2 = TextNode("This is a text node", "bold", "https://google.com/")
        self.assertNotEqual(node, node2)

    def testTextDifferent(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is different a text node", "bold", None)
        self.assertNotEqual(node, node2)

    def testTypeDiffernet(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "italics", None)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()