from .enums import InlineTitleType, BlockFrontColors, BlockBackColors

class RichText:
    """
    definition: https://www.wolai.com/uPvBQMVskPHHhxzKQBzt2a#36knqaDuXsgMMavHbAk81v
    """
    def __init__(self, 
                 type: InlineTitleType, 
                 title: str, 
                 bold: bool = False, 
                 italic: bool = False, 
                 underline: bool = False, 
                 highlight: bool = False, 
                 strikethrough: bool = False, 
                 inline_code: bool = False, 
                 front_color: BlockFrontColors = None, 
                 back_color: BlockBackColors = None):
        self.type = type
        self.title = title
        self.bold = bold
        self.italic = italic
        self.underline = underline
        self.highlight = highlight
        self.strikethrough = strikethrough
        self.inline_code = inline_code
        self.front_color = front_color
        self.back_color = back_color
