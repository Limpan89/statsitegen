

class HTMLNode:
    
    def __init__(self, tag:str=None, value:str=None, children:list['HTMLNode']=None, props:dict[str,str]=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self) -> str:
        raise NotImplementedError
    
    def props_to_html(self) -> str:
        if self.props is not None:
            attributes = []
            for k, v in self.props.items():
                attributes.append(f' {k}="{v}"')
            return "".join(attributes)
        return ""
        
    def __eq__(self, other: 'HTMLNode') -> bool:
        return (isinstance(other, HTMLNode)
            and self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props)
        
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    
class LeafNode(HTMLNode):
    
    def __init__(self,tag:str=None, value:str="", props:dict[str,str]=None):
        super().__init__(tag, value, None, props)
        
    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("The value of a LeafNode must not be None")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"