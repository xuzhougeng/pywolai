from enum import Enum
from pywolai.enums import InlineTitleType
from pywolai.enums import BlockFrontColors
from pywolai.enums import BlockBackColors


class RichText(Enum):
    """
    https://www.wolai.com/wolai/uPvBQMVskPHHhxzKQBzt2a
    """
    TYPE = InlineTitleType # 行内标题类型
    TITLE = str # 标题
    BOLD = bool # 是否加粗
    ITALIC = bool # 是否斜体
    UNDERLINE = bool # 是否下划线
    HIGHLIGHT = bool # 是否高亮
    STRIKETHROUGH = bool # 是否删除线
    INLINE_CODE = bool # 是否行内代码
    FRONT_COLOR = BlockFrontColors # 前景色
    BACK_COLOR = BlockBackColors # 背景色




