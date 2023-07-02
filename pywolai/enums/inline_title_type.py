from enum import Enum

class InlineTitleType(Enum):
    TEXT = "text"                 # "文字"
    LINK = "link"                 # "行内链接"
    BI_LINK =  "bi_link"          # "行内引用"
    COMMENT =  "comment"          # "行内评论"
    EQUATION = "equaiton"         # "行内公式"
    FONT_AWESOME = "font_awesome" # "行内FontAwesome"
    MENTION = "mention"           # "行内提醒"
    NOTE =  "note"                # "行内注释"
    FOOTNOTE = "footnote"         # "行内脚注"
