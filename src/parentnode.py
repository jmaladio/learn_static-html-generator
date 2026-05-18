from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError(f"Invalid parent node")
        if self.children == None or len(self.children) == 0:
            raise ValueError(f"The parent node doesn't have a child")
        
        html_format = f"<{self.tag}>"
        for child in self.children:
            html_format += child.to_html()
        html_format += f"</{self.tag}>"
        return html_format

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.value}, {self.children}, {self.props})"