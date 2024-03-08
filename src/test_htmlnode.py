import unittest

from htmlnode import HTMLNode


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
        

if __name__ == "__main__":
    unittest.main()