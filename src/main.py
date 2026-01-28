from textnode import TextNode, TextType

def main():
    testnode = TextNode("This is some Text", TextType.BOLD, "https://krieten.com")
    print(testnode)

if __name__ == "__main__":
    main()
