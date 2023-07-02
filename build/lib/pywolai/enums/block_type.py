from enum import Enum


class BlockTypes(Enum):
    """块类型
    https://www.wolai.com/jrmyYiJbEwmF65iQzLFZuK
    """
    ROW = "row"  # "分栏行"
    COLUMN = "column"  # "分栏列"
    TEXT = "text"  # "文本"
    PAGE = "page"  # "页面"
    CODE = "code"  # "代码"
    FILE = "file"  # "文件"
    EMBED = "embed"  # "嵌入"
    VIDEO = "video"  # "视频"
    AUDIO = "audio"  # "音频"
    IMAGE = "image"  # "图像"
    QUOTE = "quote"  # "引用"
    CALLOUT = "callout"  # "着重"
    DIVIDER = "divider"  # "分隔符"
    DATABASE = "database"  # "数据库"
    PROGRESS_BAR = "progress_bar"  # "进度条"
    BOOKMARK = "bookmark"  # "书签"
    HEADING = "heading"  # "标题"
    ENUM_LIST = "enum_list"  # "有序列表"
    TODO_LIST = "todo_list"  # "任务列表"
    TODO_LIST_PRO = "todo_list_pro"  # "高级任务列表"
    BULL_LIST = "bull_list"  # "无序列表"
    TOGGLE_LIST = "toggle_list"  # "折叠列表"
    SIMPLE_TABLE = "simple_table"  # "简单表格"
    BLOCK_EQUATION = "block_equation"  # "公式块"
    TEMPLATE_BUTTON = "template_button"  # "模板按钮"
    MEETING = "meeting"  # "会议"
    REFERENCE = "reference"  # "引用"

