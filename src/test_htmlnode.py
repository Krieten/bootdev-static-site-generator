import unittest

from htmlnode import HTMLNode, LeafNode

# HTMLNode Tests

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        testprop = {
            "href": "https://google.com",
            "target": "_blank"
        }
        node = HTMLNode("p", "Hallo" , None, testprop)
        self.assertEqual(node.props_to_html(),' href="https://google.com" target="_blank"')
    
    def test_to_html_raise(self):
        node = HTMLNode("p", "Hallo")
        with self.assertRaises(NotImplementedError):
            node.to_html()
    
    def test_init(self):
        props = {"class": "text"}
        children = []
        node = HTMLNode("p", "Hello", children, props)

        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.children, children)
        self.assertEqual(node.props, props)

# LeafNode Tests

    def test_leaf_to_html(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')


if __name__ == "__main__":
    unittest.main()