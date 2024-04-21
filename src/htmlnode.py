class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props= None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        results = ""
        for prop in self.props:
            results += f' {prop}="{self.props[prop]}"'
        return results

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None, children = None, props= None):
        if children != None:
            raise ValueError("LeafNodes can not have children")
        if value == None:
            raise ValueError("LeafNodes must have a value")
        super().__init__(tag, value, children, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNodes must have a value")
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"