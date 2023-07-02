from typing import List, Optional

from pywolai.enums import RichText, BlockTypes

from pywolai.enums import BlockBackColors, BlockFrontColors, TextAlign, BlockAlign

class BlockFormat:
    """
    Block format
    """
    def __init__(
        self,
        id: str,
        parent_id: str,
        parent_type: str,
        page_id: Optional[str],
        children: Optional[dict],
        type: BlockTypes,
        content: List[RichText],
        version: int,
        created_by: str,
        created_at: int,
        edited_by: str,
        edited_at: int,
        block_front_color: Optional[BlockFrontColors] = None,
        block_back_color: Optional[BlockBackColors] = None,
        text_alignment: Optional[TextAlign] = None,
        block_alignment: Optional[BlockAlign] = None,
        **kwargs
    ):
        self.id = id
        self.parent_id = parent_id 
        self.parent_type = parent_type
        self.page_id = page_id
        self.children = children
        self.type = type 
        self.content = content
        self.version = version
        self.created_by = created_by
        self.created_at = created_at
        self.edited_by = edited_by
        self.edited_at = edited_at
        self.block_front_color = block_front_color
        self.block_back_color = block_back_color
        self.text_alignment = text_alignment
        self.block_alignment = block_alignment
        self.other_fields = kwargs

    def __repr__(self) -> str:
        return f"ID: {self.id}\nType: {self.type}\n Content: {self.content}>"
    
    def __str__(self) -> str:
        return f"ID: {self.id}\nType: {self.type}\n Content: {self.content}>"