class HTMLNode():
    def __init__(self,tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        html = ""
        for key, value in self.props.items():
            html += f' {key}="{value}"'
        return html
    
    def __repr__(self):
        return f'{self.tag}, {self.value}, {self.children}, {self.props}'
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("Value Missing")
        if not self.tag:
            return self.value
        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        
    def __repr__(self):
        return f'{self.tag}, {self.value}, {self.props}'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag Missing")
        if not self.children:
            raise ValueError("Children Missing")
        else:
            html = ""
            html += f'<{self.tag}{self.props_to_html()}>'
            for child in self.children:
                html += child.to_html()
            html += f'</{self.tag}>'
            return html