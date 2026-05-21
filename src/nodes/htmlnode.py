class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        html_attributes = ""

        if self.props == None or len(self.props) == 0:
            return html_attributes
        
        for prop in self.props:
            new_attr = f" {prop}=\"{self.props[prop]}\""
            html_attributes += new_attr
        
        return html_attributes

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
   