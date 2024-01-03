from pywolai.enums import BlockTypes


class DatabaseRowDataItemFormat:
    """
    Database format column
    """
    def __init__(
            self,
            type: BlockTypes,
            value: str,
    ):
        self.id = id
        self.type = type
        self.value = value


class DatabaseRowDataFormat:
    """
    Database format column
    """
    def __init__(
            self,
            标题: DatabaseRowDataItemFormat,
            标签: DatabaseRowDataItemFormat,
            字段名: DatabaseRowDataItemFormat,
    ):
        self.id = id
        self.标题 = 标题
        self.标签 = 标签
        self.字段名 = 字段名



class DatabaseRowFormat:
    """
    Database format row
    """
    def __init__(
            self,
            page_id: str,
            data: DatabaseRowDataFormat,
    ):
        self.id = id
        self.page_id = page_id
        self.data = data


class DatabaseFormat:
    """
    Database format
    """
    def __init__(
            self,
            column_order: [str],
            rows: [DatabaseRowFormat],
            **kwargs
    ):
        self.column_order = column_order
        self.rows = rows
        self.other_fields = kwargs

