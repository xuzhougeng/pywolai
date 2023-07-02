from typing import List, Optional, Union
from pywolai.enums import BlockTypes, RichText




# CreateRichText定义为
# string 
# RichText 数组
# RichText  数组
# 不传递
CreateRichText = Union[str, RichText, List[Union[str, RichText]]]


# 基础 Block 类
class Block:
    """https://www.wolai.com/wolai/b6XgbNCMsnfnnsEfa2jk1z
    """
    def __init__(self, type: BlockTypes, content: Optional[CreateRichText]=None):
        self.type = type
        self.content = content

    def to_dict(self):
        return {
            "type": self.type.value,
            "content": self.content
        }


# 文本块
class TextBlock(Block):
    def __init__(self, content: Optional[CreateRichText]=None):
        super().__init__(BlockTypes.TEXT, content)

# 标题块
class HeadingBlock(Block):
    def __init__(self, level: int, toggle: Optional[bool]=False, content: Optional[CreateRichText]=None):
        super().__init__(BlockTypes.HEADING, content)
        self.level = level
        self.toggle = toggle
    
    def to_dict(self):
        return super().to_dict().update({
            "level": self.level,
            "toggle": self.toggle
        })

# TODO: 页面块
class PageBlock(Block):
    pass

# TODO:代码块
class CodeBlock(Block):
    pass

