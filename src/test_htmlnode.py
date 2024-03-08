import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode()
        node2 = HTMLNode()
        node3 = HTMLNode("This is a Tag", "This is a Value!!!")
        node4 = HTMLNode("This is a Tag", "This is a Value!!!")
        self.assertEqual(node, node2)
        self.assertEqual(node3, node4)
        
    def test_not_eq(self):
        node = HTMLNode()
        node2 = HTMLNode("This is a Tag", "This is a Value!!!")
        self.assertNotEqual(node, node2)
        
    def test_props_to_html(self):
        node = node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
        

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", None)
        node2 = LeafNode(value="This is a paragraph of text.")
        node3 = LeafNode("p", "This is a paragraph of text.")
        node4 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        with self.assertRaises(ValueError):
            node.to_html()
        self.assertEqual(node2.to_html(), "This is a paragraph of text.")
        self.assertEqual(node3.to_html(), "<p>This is a paragraph of text.</p>")
        self.assertEqual(node4.to_html(), '<a href="https://www.google.com">Click me!</a>')
        
        

if __name__ == "__main__":
    unittest.main()