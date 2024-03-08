class TextNode:
    
    def __init__(self, text: str, text_type: str, url:str=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        
    def __eq__(self, other: 'TextNode') -> bool:
        return (isinstance(other, TextNode)
            and self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url)

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"