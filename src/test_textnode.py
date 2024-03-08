import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
        
    def test_url(self):
        node = TextNode("This is a text node", "bold", "www.internet.com")
        node2 = TextNode("This is a text node", "bold")
        self.assertIsNotNone(node.url)
        self.assertIsNone(node2.url)
        
    def test_not_eq(self):
        node = TextNode("This is a text node", "bold", "www.internet.com")
        node2 = TextNode("This is a text node", "bold")
        node3 = TextNode("This is a text node", "italics")
        node4 = TextNode("Text Node", "italics")
        self.assertNotEqual(node, node2)
        self.assertNotEqual(node2, node3)
        self.assertNotEqual(node3, node4)
        self.assertNotEqual(node, node4)


if __name__ == "__main__":
    unittest.main()